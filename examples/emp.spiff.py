
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser import SpiffBpmnParser
from SpiffWorkflow.task import TaskState

from SpiffWorkflow.dmn.serializer import BusinessRuleTaskConverter
from SpiffWorkflow.spiff.serializer import BoundaryEventConverter
from SpiffWorkflow.spiff.serializer import CallActivityTaskConverter
from SpiffWorkflow.spiff.serializer import EndEventConverter
from SpiffWorkflow.spiff.serializer import IntermediateCatchEventConverter
from SpiffWorkflow.spiff.serializer import IntermediateThrowEventConverter
from SpiffWorkflow.spiff.serializer import ManualTaskConverter
from SpiffWorkflow.spiff.serializer import NoneTaskConverter
from SpiffWorkflow.spiff.serializer import ReceiveTaskConverter
from SpiffWorkflow.spiff.serializer import ScriptTaskConverter
from SpiffWorkflow.spiff.serializer import SendTaskConverter
from SpiffWorkflow.spiff.serializer import ServiceTaskConverter
from SpiffWorkflow.spiff.serializer import StartEventConverter
from SpiffWorkflow.spiff.serializer import SubWorkflowTaskConverter
from SpiffWorkflow.spiff.serializer import TransactionSubprocessConverter
from SpiffWorkflow.spiff.serializer import UserTaskConverter

from SpiffWorkflow.bpmn.serializer import BpmnWorkflowSerializer

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
serialized = {'data': {}, 'last_task': None, 'success': True, 'tasks': {'510f2060-0550-4a95-8d37-f01bd199d0e7': {'id': '510f2060-0550-4a95-8d37-f01bd199d0e7', 'parent': None, 'children': ['a3fdd700-7416-4b2b-bad2-dfcd086d0d1f'], 'last_state_change': 1667411751.6613412, 'state': 32, 'task_spec': 'Root', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, 'a3fdd700-7416-4b2b-bad2-dfcd086d0d1f': {'id': 'a3fdd700-7416-4b2b-bad2-dfcd086d0d1f', 'parent': '510f2060-0550-4a95-8d37-f01bd199d0e7', 'children': ['987fd6af-b79c-4c4d-8349-86d35dab4b20'], 'last_state_change': 1667411751.661467, 'state': 16, 'task_spec': 'Start', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, '987fd6af-b79c-4c4d-8349-86d35dab4b20': {'id': '987fd6af-b79c-4c4d-8349-86d35dab4b20', 'parent': 'a3fdd700-7416-4b2b-bad2-dfcd086d0d1f', 'children': ['bafb71a7-91e6-4c35-a94b-88304660ebe5'], 'last_state_change': 1667411751.661376, 'state': 4, 'task_spec': 'StartEvent_1', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, 'bafb71a7-91e6-4c35-a94b-88304660ebe5': {'id': 'bafb71a7-91e6-4c35-a94b-88304660ebe5', 'parent': '987fd6af-b79c-4c4d-8349-86d35dab4b20', 'children': ['8598ddf2-2524-4910-95f2-757feed14947'], 'last_state_change': 1667411751.6613917, 'state': 4, 'task_spec': 'EndEvent_0q4qzl9', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, '8598ddf2-2524-4910-95f2-757feed14947': {'id': '8598ddf2-2524-4910-95f2-757feed14947', 'parent': 'bafb71a7-91e6-4c35-a94b-88304660ebe5', 'children': ['e2342386-aba0-40df-a2b0-7618d95c67e6'], 'last_state_change': 1667411751.6614044, 'state': 4, 'task_spec': 'empty_workflow.EndJoin', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, 'e2342386-aba0-40df-a2b0-7618d95c67e6': {'id': 'e2342386-aba0-40df-a2b0-7618d95c67e6', 'parent': '8598ddf2-2524-4910-95f2-757feed14947', 'children': [], 'last_state_change': 1667411751.661419, 'state': 4, 'task_spec': 'End', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}}, 'root': '510f2060-0550-4a95-8d37-f01bd199d0e7', 'spec': {'name': 'empty_workflow', 'description': 'empty_workflow', 'file': 'examples/emp.bpmn', 'task_specs': {'Start': {'id': 'empty_workflow_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'empty_workflow.EndJoin': {'id': 'empty_workflow_2', 'name': 'empty_workflow.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['EndEvent_0q4qzl9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'empty_workflow_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['empty_workflow.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'empty_workflow_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['EndEvent_0q4qzl9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 179.0, 'y': 99.0}, 'outgoing_sequence_flows': {'EndEvent_0q4qzl9': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'SequenceFlow_0lvudp8': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'EndEvent_0q4qzl9': {'id': 'empty_workflow_5', 'name': 'EndEvent_0q4qzl9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['empty_workflow.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 432.0, 'y': 99.0}, 'outgoing_sequence_flows': {'empty_workflow.EndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'EndEvent_0q4qzl9.ToEndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'empty_workflow_6', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}, 'subprocess_specs': {'empty_workflow': {'name': 'empty_workflow', 'description': 'empty_workflow', 'file': 'examples/emp.bpmn', 'task_specs': {'Start': {'id': 'empty_workflow_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'empty_workflow.EndJoin': {'id': 'empty_workflow_2', 'name': 'empty_workflow.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['EndEvent_0q4qzl9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'empty_workflow_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['empty_workflow.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'empty_workflow_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['EndEvent_0q4qzl9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 179.0, 'y': 99.0}, 'outgoing_sequence_flows': {'EndEvent_0q4qzl9': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'SequenceFlow_0lvudp8': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'EndEvent_0q4qzl9': {'id': 'empty_workflow_5', 'name': 'EndEvent_0q4qzl9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['empty_workflow.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 432.0, 'y': 99.0}, 'outgoing_sequence_flows': {'empty_workflow.EndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'EndEvent_0q4qzl9.ToEndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'empty_workflow_6', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}}, 'subprocesses': {}, 'bpmn_messages': []}

wf = serializer.workflow_from_dict(serialized)
wf.do_engine_steps()
print(wf.data)
