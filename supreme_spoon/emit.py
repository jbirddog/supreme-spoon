
# TODO: support other emitters, this is really a BasicCLIEmitter
class Emitter:

    @classmethod
    def spec_converters_array(cls, spec_converters):
        return f"[{', '.join(spec_converters)}]"

    @classmethod
    def build_imports(cls, spec_converters, spec_types):
        imports = []

        if "Script Task" in spec_types:
            imports.append("from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine")

        imports.append("from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer")

        for spec_converter in spec_converters:
            imports.append(f"from SpiffWorkflow.spiff.serializer.task_spec_converters import {spec_converter}")

        return imports

    @classmethod
    def build_task_handlers(cls, grouped_task_metadata):
        task_handlers = []
        task_handler_map = {}
        if "manual" in grouped_task_metadata:
            task_handlers.append("""
    def handle_manual_task(instructionsForEndUser=None, description=None, documentation=None):
        def _handler(task):
            print("\\nManual Task:\\n")
            if description:
                print(f"\\t{description.title()}\\n")
            if instructionsForEndUser:
                print(f"\\t{instructionsForEndUser}\\n")
            if documentation:
                print(f"\\t{documentation}\\n")
            input("Press enter to continue")
        return _handler""")

            for metadata in grouped_task_metadata["manual"]:
                task_handler_map[metadata[0]] = ("handle_manual_task", metadata[1])

        output = task_handlers

        if len(output) > 0:
            output.append("""
    TASK_HANDLERS = {""")

            for k, v in task_handler_map.items():
                output.append(f'        "{k}": {v[0]}(**{v[1]}),')

            output.append("\t}")

        #task_handlers.append(f"TASK_HANDLERS = {task_handler_map}")

        return output

    @classmethod
    def emit(cls, 
        class_name, 
        serialized_workflow, 
        serializer_version, 
        spec_converters, 
        spec_types,
        grouped_task_metadata, 
        output_filename
    ):
        imports = cls.build_imports(spec_converters, spec_types)
        sc_array = cls.spec_converters_array(spec_converters)

        output = ["# GENERATED by Supreme Spoon", ""]
        output += imports

        # TODO: break this out more so we can get more granular based on individual workflows
        output += [f"""

class {class_name}:
    def __init__(self, scripting_additions=None):
        self.scripting_additions = scripting_additions"""]

        output += cls.build_task_handlers(grouped_task_metadata)

        output += [f"""
    def get_serializer(self):
        spec_converters = {sc_array}
        spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(spec_converters)
        serializer = BpmnWorkflowSerializer(spec_converter, version="{serializer_version}")
        return serializer

    # TODO: restore
    def get_workflow(self):
        workflow = self.get_serializer().workflow_from_dict(self.SERIALIZED_WORKFLOW)

        if self.scripting_additions is not None:
            workflow.script_engine = PythonScriptEngine(scripting_additions=self.scripting_additions)

        return workflow

    def run(self):
        workflow = self.get_workflow()
        workflow.do_engine_steps()
        while not workflow.is_completed():
            ready_tasks = workflow.get_ready_user_tasks()
            for task in ready_tasks:
                if task.task_spec.name in self.TASK_HANDLERS:
                    self.TASK_HANDLERS[task.task_spec.name](task)
                task.complete()
            workflow.refresh_waiting_tasks()
            workflow.do_engine_steps()

        return workflow.data

    SERIALIZED_WORKFLOW = {serialized_workflow}
"""
        ]

        with open(output_filename, "w") as f:
            f.write("\n".join(output))
