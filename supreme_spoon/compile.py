from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter


SERIALIZER_VERSION = "1.0-supreme-spoon"
wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
    [
        ManualTaskConverter,
        ScriptTaskConverter,
    ]
)
_serializer = BpmnWorkflowSerializer(wf_spec_converter, version=SERIALIZER_VERSION)


class Compiler:

    @classmethod
    def parse_workflow(cls, parser, process, bpmn_files):
        parser.add_bpmn_files(bpmn_files)
        top_level = parser.get_spec(process)
        subprocesses = parser.find_all_specs()
        return BpmnWorkflow(top_level, subprocesses)

    @classmethod
    def compile(cls, process, input_filename, output_filename):
        parser = SpiffBpmnParser()
        wf = cls.parse_workflow(parser, process, [input_filename])
        tasks = wf.get_tasks()
        for task in tasks:
            print(task.task_spec.spec_type)
        serialized = _serializer.workflow_to_dict(wf)

        with open(output_filename, "w") as f:
            f.write(f"""
from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter


SERIALIZER_VERSION = "{SERIALIZER_VERSION}"
wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
    [
        ManualTaskConverter,
        ScriptTaskConverter,
    ]
)
serializer = BpmnWorkflowSerializer(wf_spec_converter, version=SERIALIZER_VERSION)
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
