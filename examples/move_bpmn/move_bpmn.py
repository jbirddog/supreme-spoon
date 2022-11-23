# GENERATED by Supreme Spoon

# TODO: be smarter about when to import this, possibly detect scripting_additions
from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine
from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter


class MoveBPMNFiles:
    def __init__(self, scripting_additions=None):
        self.scripting_additions = scripting_additions

    def get_serializer(self):
        spec_converters = [ScriptTaskConverter]
        spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(spec_converters)
        serializer = BpmnWorkflowSerializer(spec_converter, version="1.0-supreme-spoon")
        return serializer

    # TODO: restore
    def get_workflow(self):
        workflow = self.get_serializer().workflow_from_dict(self.SERIALIZED)

        if self.scripting_additions is not None:
            workflow.script_engine = PythonScriptEngine(scripting_additions=self.scripting_additions)

        return workflow

    def run(self):
        workflow = self.get_workflow()
        workflow.do_engine_steps()
        while not workflow.is_completed():
            ready_tasks = workflow.get_ready_user_tasks()
            for task in ready_tasks:
                task.complete()
            workflow.refresh_waiting_tasks()
            workflow.do_engine_steps()

        return workflow.data

    SERIALIZED = {'data': {}, 'last_task': None, 'success': True, 'tasks': {'079c3879-04b8-421a-a982-b7ecd0580737': {'id': '079c3879-04b8-421a-a982-b7ecd0580737', 'parent': None, 'children': ['fcba0b8e-3a31-480d-8c46-829f2a84838a'], 'last_state_change': 1669233636.5361753, 'state': 32, 'task_spec': 'Root', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'fcba0b8e-3a31-480d-8c46-829f2a84838a': {'id': 'fcba0b8e-3a31-480d-8c46-829f2a84838a', 'parent': '079c3879-04b8-421a-a982-b7ecd0580737', 'children': ['42c9d7c7-d193-486e-81a1-e3836cff3b93'], 'last_state_change': 1669233636.5363085, 'state': 16, 'task_spec': 'Start', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '42c9d7c7-d193-486e-81a1-e3836cff3b93': {'id': '42c9d7c7-d193-486e-81a1-e3836cff3b93', 'parent': 'fcba0b8e-3a31-480d-8c46-829f2a84838a', 'children': ['5ce4f53c-853b-474d-9e89-7bb565f6e604'], 'last_state_change': 1669233636.5362005, 'state': 4, 'task_spec': 'StartEvent_1', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '5ce4f53c-853b-474d-9e89-7bb565f6e604': {'id': '5ce4f53c-853b-474d-9e89-7bb565f6e604', 'parent': '42c9d7c7-d193-486e-81a1-e3836cff3b93', 'children': ['b1bd231a-4968-4bd2-9543-9cf4f8ca6684'], 'last_state_change': 1669233636.5362165, 'state': 4, 'task_spec': 'Activity_0jvfn7c', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'b1bd231a-4968-4bd2-9543-9cf4f8ca6684': {'id': 'b1bd231a-4968-4bd2-9543-9cf4f8ca6684', 'parent': '5ce4f53c-853b-474d-9e89-7bb565f6e604', 'children': ['3529d6c7-9f61-4466-91f1-264861dd61df'], 'last_state_change': 1669233636.5362475, 'state': 4, 'task_spec': 'Event_0f7r3q9', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '3529d6c7-9f61-4466-91f1-264861dd61df': {'id': '3529d6c7-9f61-4466-91f1-264861dd61df', 'parent': 'b1bd231a-4968-4bd2-9543-9cf4f8ca6684', 'children': ['b107f5a6-1782-4a79-8737-2fae787f79ba'], 'last_state_change': 1669233636.5362582, 'state': 4, 'task_spec': 'Process_qpfr71f.EndJoin', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'b107f5a6-1782-4a79-8737-2fae787f79ba': {'id': 'b107f5a6-1782-4a79-8737-2fae787f79ba', 'parent': '3529d6c7-9f61-4466-91f1-264861dd61df', 'children': [], 'last_state_change': 1669233636.5362694, 'state': 4, 'task_spec': 'End', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}}, 'root': '079c3879-04b8-421a-a982-b7ecd0580737', 'spec': {'name': 'Process_qpfr71f', 'description': 'MoveBPMNFiles', 'file': 'examples/move_bpmn/move_bpmn.bpmn', 'task_specs': {'Start': {'id': 'Process_qpfr71f_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'Process_qpfr71f.EndJoin': {'id': 'Process_qpfr71f_2', 'name': 'Process_qpfr71f.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_0f7r3q9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'Process_qpfr71f_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Process_qpfr71f.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'Process_qpfr71f_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Activity_0jvfn7c'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 179.0, 'y': 159.0}, 'outgoing_sequence_flows': {'Activity_0jvfn7c': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0my7q5j': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Activity_0jvfn7c': {'id': 'Process_qpfr71f_5', 'name': 'Activity_0jvfn7c', 'description': 'build directory paths', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['Event_0f7r3q9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 270.0, 'y': 137.0}, 'outgoing_sequence_flows': {'Event_0f7r3q9': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0vsyo0z': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\nfrom pathlib import Path\n\nhome_dir = Path.home()\ndownload_dir = os.path.join(home_dir, "Downloads")\nproject_dir = os.path.join(home_dir, "projects", "github", "jbirddog", "supreme-spoon")', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_0f7r3q9': {'id': 'Process_qpfr71f_6', 'name': 'Event_0f7r3q9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0jvfn7c'], 'outputs': ['Process_qpfr71f.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 432.0, 'y': 159.0}, 'outgoing_sequence_flows': {'Process_qpfr71f.EndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_0f7r3q9.ToEndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'Process_qpfr71f_7', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}, 'subprocess_specs': {'Process_qpfr71f': {'name': 'Process_qpfr71f', 'description': 'MoveBPMNFiles', 'file': 'examples/move_bpmn/move_bpmn.bpmn', 'task_specs': {'Start': {'id': 'Process_qpfr71f_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'Process_qpfr71f.EndJoin': {'id': 'Process_qpfr71f_2', 'name': 'Process_qpfr71f.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_0f7r3q9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'Process_qpfr71f_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Process_qpfr71f.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'Process_qpfr71f_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Activity_0jvfn7c'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 179.0, 'y': 159.0}, 'outgoing_sequence_flows': {'Activity_0jvfn7c': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0my7q5j': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Activity_0jvfn7c': {'id': 'Process_qpfr71f_5', 'name': 'Activity_0jvfn7c', 'description': 'build directory paths', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['Event_0f7r3q9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 270.0, 'y': 137.0}, 'outgoing_sequence_flows': {'Event_0f7r3q9': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0vsyo0z': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\nfrom pathlib import Path\n\nhome_dir = Path.home()\ndownload_dir = os.path.join(home_dir, "Downloads")\nproject_dir = os.path.join(home_dir, "projects", "github", "jbirddog", "supreme-spoon")', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_0f7r3q9': {'id': 'Process_qpfr71f_6', 'name': 'Event_0f7r3q9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0jvfn7c'], 'outputs': ['Process_qpfr71f.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 432.0, 'y': 159.0}, 'outgoing_sequence_flows': {'Process_qpfr71f.EndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_0f7r3q9.ToEndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'Process_qpfr71f_7', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}}, 'subprocesses': {}, 'bpmn_messages': []}