from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter

from emit import Emitter

class Dependencies:

    SPEC_CONVERTERS = {
        "Manual Task": (ManualTaskConverter, "ManualTaskConverter"),
        "Script Task": (ScriptTaskConverter, "ScriptTaskConverter"),
    }

    @classmethod
    def compile_time_spec_converters(cls):
        def sc_cls(tup):
            return tup[0]

        return list(map(sc_cls, cls.SPEC_CONVERTERS.values()))
    
    @classmethod
    def runtime_spec_converters(cls, tasks):
        deps = set()
        for task in tasks:
            spec_type = task.task_spec.spec_type
            if spec_type == "Manual Task":
                print(f"{spec_type}: {task.task_spec.name}")
                print(task.task_spec.description.title())
                print(task.task_spec.extensions)
            if spec_type in cls.SPEC_CONVERTERS:
                deps.add(cls.SPEC_CONVERTERS[spec_type][1])
        return sorted(list(deps))


class Compiler:
    SERIALIZER_VERSION = "1.0-supreme-spoon"

    @classmethod
    def parse_workflow(cls, process, bpmn_files):
        parser = SpiffBpmnParser()
        parser.add_bpmn_files(bpmn_files)
        top_level = parser.get_spec(process)
        subprocesses = parser.find_all_specs()
        return BpmnWorkflow(top_level, subprocesses)

    @classmethod
    def get_serializer(cls):
        spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
            Dependencies.compile_time_spec_converters()
        )
        return BpmnWorkflowSerializer(spec_converter, version=cls.SERIALIZER_VERSION)

    @classmethod
    def build_manual_task_metadata(cls, task):
        task_spec = task.task_spec
        metadata = task_spec.extensions or {}
        if task_spec.description is not None:
            metadata["description"] = task_spec.description
        if task_spec.documentation is not None:
            metadata["documentation"] = task_spec.documentation
        return (task_spec.name, metadata)

    @classmethod
    def build_engine_step_metadata(cls, task):
        return task.task_spec.name

    @classmethod
    def build_grouped_task_metadata(cls, tasks):
        group_builder = {
            "Manual Task": ("manual", cls.build_manual_task_metadata),
        }
        default_group_builder = ("engine", cls.build_engine_step_metadata)
        groups = {}
        for task in tasks:
            spec_type = task.task_spec.spec_type
            group_key, metadata_builder = group_builder.get(spec_type, default_group_builder)
            if group_key not in groups:
                groups[group_key] = []
            group_metadata = groups[group_key]
            group_metadata.append(metadata_builder(task))
        return groups

    @classmethod
    def compile(cls, process, input_filename, output_filename):
        workflow = cls.parse_workflow(process, [input_filename])
        tasks = workflow.get_tasks()
        serialized = cls.get_serializer().workflow_to_dict(workflow)
        spec_converters = Dependencies.runtime_spec_converters(tasks)
        grouped_task_metadata = cls.build_grouped_task_metadata(tasks)
        print(grouped_task_metadata)

        Emitter.emit(process, serialized, cls.SERIALIZER_VERSION, spec_converters, grouped_task_metadata, output_filename)

if __name__ == "__main__":
    import sys

    # TODO: argparse
    #process = sys.argv[1]
    #input_filename = sys.argv[2]
    #output_filename = sys.argv[3]

    process = "MoveBPMNFiles"
    input_filename = "examples/move_bpmn/move_bpmn.bpmn"
    output_filename = "examples/move_bpmn/move_bpmn.py"

    Compiler.compile(process, input_filename, output_filename)
