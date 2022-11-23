from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter

from emit import Emitter


class Compiler:
    SERIALIZER_VERSION = "1.0-supreme-spoon"

    SPEC_CONVERTERS = {
        "ManualTask": ManualTaskConverter,
        "ScriptTask": ScriptTaskConverter,
    }

    @classmethod
    def parse_workflow(cls, process, bpmn_files):
        parser = SpiffBpmnParser()
        parser.add_bpmn_files(bpmn_files)
        top_level = parser.get_spec(process)
        subprocesses = parser.find_all_specs()
        return BpmnWorkflow(top_level, subprocesses)

    @classmethod
    def get_serializer(cls):
        wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
            cls.SPEC_CONVERTERS.values()
        )
        return BpmnWorkflowSerializer(wf_spec_converter, version=cls.SERIALIZER_VERSION)

    @classmethod
    def compile(cls, process, input_filename, output_filename):
        wf = cls.parse_workflow(process, [input_filename])
        tasks = wf.get_tasks()
        for task in tasks:
            print(task.task_spec.spec_type)
        serialized = cls.get_serializer().workflow_to_dict(wf)

        Emitter.emit(serialized, cls.SERIALIZER_VERSION, output_filename)

if __name__ == "__main__":
    import sys

    # TODO: argparse
    #process = sys.argv[1]
    #input_filename = sys.argv[2]
    #output_filename = sys.argv[3]

    process = "Process_qpfr71f"
    input_filename = "examples/copybpmn/copybpmn.bpmn"
    output_filename = "examples/copybpmn/copybpmn.py"

    Compiler.compile(process, input_filename, output_filename)
