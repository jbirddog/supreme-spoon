
from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter
from SpiffWorkflow.task import TaskState


SERIALIZER_VERSION = "1.0-supreme-spoon"
wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
    [
        ScriptTaskConverter,
    ]
)
serializer = BpmnWorkflowSerializer(wf_spec_converter, version=SERIALIZER_VERSION)
serialized = {'data': {}, 'last_task': None, 'success': True, 'tasks': {'d38a217c-d8fe-4fcd-9660-2d9ea461d3e1': {'id': 'd38a217c-d8fe-4fcd-9660-2d9ea461d3e1', 'parent': None, 'children': ['dfd2e6c9-d10a-4d43-a955-9b52e19bb898'], 'last_state_change': 1667439670.1317604, 'state': 32, 'task_spec': 'Root', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, 'dfd2e6c9-d10a-4d43-a955-9b52e19bb898': {'id': 'dfd2e6c9-d10a-4d43-a955-9b52e19bb898', 'parent': 'd38a217c-d8fe-4fcd-9660-2d9ea461d3e1', 'children': ['01fd3b7e-261d-4021-9795-50d2f6a727f7'], 'last_state_change': 1667439670.131879, 'state': 16, 'task_spec': 'Start', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, '01fd3b7e-261d-4021-9795-50d2f6a727f7': {'id': '01fd3b7e-261d-4021-9795-50d2f6a727f7', 'parent': 'dfd2e6c9-d10a-4d43-a955-9b52e19bb898', 'children': ['e0e2522f-3244-41aa-acb6-aeb63d720cfe'], 'last_state_change': 1667439670.131794, 'state': 4, 'task_spec': 'StartEvent_1', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, 'e0e2522f-3244-41aa-acb6-aeb63d720cfe': {'id': 'e0e2522f-3244-41aa-acb6-aeb63d720cfe', 'parent': '01fd3b7e-261d-4021-9795-50d2f6a727f7', 'children': ['575cc526-842e-464c-adb7-62e88988dee9'], 'last_state_change': 1667439670.1318088, 'state': 4, 'task_spec': 'EndEvent_0q4qzl9', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, '575cc526-842e-464c-adb7-62e88988dee9': {'id': '575cc526-842e-464c-adb7-62e88988dee9', 'parent': 'e0e2522f-3244-41aa-acb6-aeb63d720cfe', 'children': ['5251813d-b860-4333-b6d9-4d131894e68e'], 'last_state_change': 1667439670.1318204, 'state': 4, 'task_spec': 'empty_workflow.EndJoin', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}, '5251813d-b860-4333-b6d9-4d131894e68e': {'id': '5251813d-b860-4333-b6d9-4d131894e68e', 'parent': '575cc526-842e-464c-adb7-62e88988dee9', 'children': [], 'last_state_change': 1667439670.1318326, 'state': 4, 'task_spec': 'End', 'triggered': False, 'workflow_name': 'empty_workflow', 'internal_data': {}, 'data': {}}}, 'root': 'd38a217c-d8fe-4fcd-9660-2d9ea461d3e1', 'spec': {'name': 'empty_workflow', 'description': 'empty_workflow', 'file': 'examples/emp.bpmn', 'task_specs': {'Start': {'id': 'empty_workflow_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'empty_workflow.EndJoin': {'id': 'empty_workflow_2', 'name': 'empty_workflow.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['EndEvent_0q4qzl9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'empty_workflow_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['empty_workflow.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'empty_workflow_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['EndEvent_0q4qzl9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 179.0, 'y': 99.0}, 'outgoing_sequence_flows': {'EndEvent_0q4qzl9': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'SequenceFlow_0lvudp8': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'EndEvent_0q4qzl9': {'id': 'empty_workflow_5', 'name': 'EndEvent_0q4qzl9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['empty_workflow.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 432.0, 'y': 99.0}, 'outgoing_sequence_flows': {'empty_workflow.EndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'EndEvent_0q4qzl9.ToEndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'empty_workflow_6', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}, 'subprocess_specs': {'empty_workflow': {'name': 'empty_workflow', 'description': 'empty_workflow', 'file': 'examples/emp.bpmn', 'task_specs': {'Start': {'id': 'empty_workflow_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'empty_workflow.EndJoin': {'id': 'empty_workflow_2', 'name': 'empty_workflow.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['EndEvent_0q4qzl9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'empty_workflow_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['empty_workflow.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'empty_workflow_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['EndEvent_0q4qzl9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 179.0, 'y': 99.0}, 'outgoing_sequence_flows': {'EndEvent_0q4qzl9': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'SequenceFlow_0lvudp8': {'id': 'SequenceFlow_0lvudp8', 'name': None, 'documentation': None, 'target_task_spec': 'EndEvent_0q4qzl9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'EndEvent_0q4qzl9': {'id': 'empty_workflow_5', 'name': 'EndEvent_0q4qzl9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['empty_workflow.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 432.0, 'y': 99.0}, 'outgoing_sequence_flows': {'empty_workflow.EndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'EndEvent_0q4qzl9.ToEndJoin': {'id': 'EndEvent_0q4qzl9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'empty_workflow.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'empty_workflow_6', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}}, 'subprocesses': {}, 'bpmn_messages': []}

wf = serializer.workflow_from_dict(serialized)
wf.do_engine_steps()
print(wf.data)
