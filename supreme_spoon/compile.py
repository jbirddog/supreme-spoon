#from backend.python_cps import PythonCPSBackend
#from frontend.bpmn import BpmnFrontend
#from util import by_id

from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.task import TaskState

from SpiffWorkflow.dmn.serializer.task_spec_converters import BusinessRuleTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import BoundaryEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import CallActivityTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import EndEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import IntermediateCatchEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import IntermediateThrowEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import NoneTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ReceiveTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import SendTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ServiceTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import StartEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import SubWorkflowTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import TransactionSubprocessConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import UserTaskConverter

from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer

SERIALIZER_VERSION = "1.0-supreme-spoon"
wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
    [
        BoundaryEventConverter,
        BusinessRuleTaskConverter,
        CallActivityTaskConverter,
        EndEventConverter,
        IntermediateCatchEventConverter,
        IntermediateThrowEventConverter,
        ManualTaskConverter,
        NoneTaskConverter,
        ReceiveTaskConverter,
        ScriptTaskConverter,
        SendTaskConverter,
        ServiceTaskConverter,
        StartEventConverter,
        SubWorkflowTaskConverter,
        TransactionSubprocessConverter,
        UserTaskConverter,
    ]
)
_serializer = BpmnWorkflowSerializer(wf_spec_converter, version=SERIALIZER_VERSION)


class Compiler:

    @classmethod
    def parse_workflow(self, parser, process, bpmn_files):
        parser.add_bpmn_files(bpmn_files)
        top_level = parser.get_spec(process)
        subprocesses = parser.find_all_specs()
        return BpmnWorkflow(top_level, subprocesses)

    @classmethod
    def compile(self, process, input_filename, output_filename):
        parser = SpiffBpmnParser()
        wf = self.parse_workflow(parser, process, [input_filename])
        #wf.do_engine_steps()
        #print(wf.data)
        #return
        serialized = _serializer.workflow_to_dict(wf)

        with open(output_filename, "w") as f:
            f.write(f"""
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.task import TaskState

from SpiffWorkflow.dmn.serializer.task_spec_converters import BusinessRuleTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import BoundaryEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import CallActivityTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import EndEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import IntermediateCatchEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import IntermediateThrowEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import NoneTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ReceiveTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import SendTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ServiceTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import StartEventConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import SubWorkflowTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import TransactionSubprocessConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import UserTaskConverter

from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer

SERIALIZER_VERSION = "1.0-supreme-spoon"
wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
    [
        BoundaryEventConverter,
        BusinessRuleTaskConverter,
        CallActivityTaskConverter,
        EndEventConverter,
        IntermediateCatchEventConverter,
        IntermediateThrowEventConverter,
        ManualTaskConverter,
        NoneTaskConverter,
        ReceiveTaskConverter,
        ScriptTaskConverter,
        SendTaskConverter,
        ServiceTaskConverter,
        StartEventConverter,
        SubWorkflowTaskConverter,
        TransactionSubprocessConverter,
        UserTaskConverter,
    ]
)
serializer = BpmnWorkflowSerializer(wf_spec_converter, version=SERIALIZER_VERSION)
serialized = {serialized}

wf = serializer.workflow_from_dict(serialized)
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

    Compiler.compile(process, input_filename, output_filename)

    # 1-1000 vanilla spiff parse/do_engine_steps = ~5s runtime on my machine
    for i in range(1, 2):
        process = "Proccess_3qizfj5"
        input_filename = "examples/pg.bpmn"
        output_filename = "examples/pg.spiff.py"

        Compiler.compile(process, input_filename, output_filename)
