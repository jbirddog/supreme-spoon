from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter
from SpiffWorkflow.task import TaskState


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
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter
from SpiffWorkflow.task import TaskState


SERIALIZER_VERSION = "1.0-supreme-spoon"
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

    #process = sys.argv[1]
    ##input_filename = sys.argv[2]
    #output_filename = sys.argv[3]

    print('\n------------------------\n')

    process = "empty_workflow"
    input_filename = "examples/emp.bpmn"
    output_filename = "examples/emp.spiff.py"

    process = "Proccess_v60ufvy"
    input_filename = "supreme_spoon/bpmn/spoon.bpmn"
    output_filename = "examples/spoon.py"

    process = "Proccess_3qizfj5"
    input_filename = "examples/man_pg.bpmn"
    output_filename = "examples/man_pg.spiff.py"

    Compiler.compile(process, input_filename, output_filename)

    # 1-1000 vanilla spiff parse/do_engine_steps = ~5s runtime on my machine
    for i in range(1, 2):
        process = "Proccess_3qizfj5"
        input_filename = "examples/pg.bpmn"
        output_filename = "examples/pg.spiff.py"

        Compiler.compile(process, input_filename, output_filename)
