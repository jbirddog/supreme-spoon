
class Emitter:

    @classmethod
    def spec_converter_imports(cls, spec_converters):
        def build_import(sc):
            return f"from SpiffWorkflow.spiff.serializer.task_spec_converters import {sc}"

        return "\n".join(map(build_import, spec_converters))

    @classmethod
    def spec_converters_array(cls, spec_converters):
        return f"[{', '.join(spec_converters)}]"

    @classmethod
    def emit(cls, serialized, serializer_version, spec_converters, output_filename):
        sc_imports = cls.spec_converter_imports(spec_converters)
        sc_array = cls.spec_converters_array(spec_converters)
        print(sc_array)
        with open(output_filename, "w") as f:
            f.write(f"""
from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
{sc_imports}


spec_converters = {sc_array}
wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(spec_converters)
serializer = BpmnWorkflowSerializer(wf_spec_converter, version="{serializer_version}")
serialized = {serialized}

wf = serializer.workflow_from_dict(serialized)
wf.do_engine_steps()

while not wf.is_completed():
    ready_tasks = wf.get_ready_user_tasks()
    for task in ready_tasks:
        task.complete()
    wf.refresh_waiting_tasks()
    wf.do_engine_steps()

print(wf.data)
""")
