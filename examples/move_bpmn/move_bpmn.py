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

    SERIALIZED = {'data': {}, 'last_task': None, 'success': True, 'tasks': {'e5f1d75a-8c99-4d01-a3b8-fc6d14996507': {'id': 'e5f1d75a-8c99-4d01-a3b8-fc6d14996507', 'parent': None, 'children': ['7b7543b8-5706-43e2-99f9-9fc2375a1c5c'], 'last_state_change': 1669243477.6123965, 'state': 32, 'task_spec': 'Root', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '7b7543b8-5706-43e2-99f9-9fc2375a1c5c': {'id': '7b7543b8-5706-43e2-99f9-9fc2375a1c5c', 'parent': 'e5f1d75a-8c99-4d01-a3b8-fc6d14996507', 'children': ['a68e46c0-7cd0-4e67-ab26-7e4979507606'], 'last_state_change': 1669243477.612554, 'state': 16, 'task_spec': 'Start', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'a68e46c0-7cd0-4e67-ab26-7e4979507606': {'id': 'a68e46c0-7cd0-4e67-ab26-7e4979507606', 'parent': '7b7543b8-5706-43e2-99f9-9fc2375a1c5c', 'children': ['f65da64f-7117-4d7e-b7d3-b8ca6322f246'], 'last_state_change': 1669243477.6124222, 'state': 4, 'task_spec': 'StartEvent_1', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'f65da64f-7117-4d7e-b7d3-b8ca6322f246': {'id': 'f65da64f-7117-4d7e-b7d3-b8ca6322f246', 'parent': 'a68e46c0-7cd0-4e67-ab26-7e4979507606', 'children': ['7e18d983-a799-49c1-bbab-c9bfb40ae361'], 'last_state_change': 1669243477.61244, 'state': 4, 'task_spec': 'Activity_0jvfn7c', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '7e18d983-a799-49c1-bbab-c9bfb40ae361': {'id': '7e18d983-a799-49c1-bbab-c9bfb40ae361', 'parent': 'f65da64f-7117-4d7e-b7d3-b8ca6322f246', 'children': ['66bb9d87-0284-446c-8269-0104a33c5928'], 'last_state_change': 1669243477.6124547, 'state': 4, 'task_spec': 'Activity_1v124g4', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '66bb9d87-0284-446c-8269-0104a33c5928': {'id': '66bb9d87-0284-446c-8269-0104a33c5928', 'parent': '7e18d983-a799-49c1-bbab-c9bfb40ae361', 'children': ['8bd679c5-e5ce-4ff9-bf47-362976fa1706'], 'last_state_change': 1669243477.6124654, 'state': 4, 'task_spec': 'Activity_1vwbjch', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '8bd679c5-e5ce-4ff9-bf47-362976fa1706': {'id': '8bd679c5-e5ce-4ff9-bf47-362976fa1706', 'parent': '66bb9d87-0284-446c-8269-0104a33c5928', 'children': ['e83ec9a7-6b91-4ab1-9dd1-2b2f6ea4d86c'], 'last_state_change': 1669243477.6124756, 'state': 4, 'task_spec': 'Activity_1onldol', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'e83ec9a7-6b91-4ab1-9dd1-2b2f6ea4d86c': {'id': 'e83ec9a7-6b91-4ab1-9dd1-2b2f6ea4d86c', 'parent': '8bd679c5-e5ce-4ff9-bf47-362976fa1706', 'children': ['eea2bcb4-2e1c-412a-9a52-d975a51fb3a9'], 'last_state_change': 1669243477.6124883, 'state': 4, 'task_spec': 'Event_0f7r3q9', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'eea2bcb4-2e1c-412a-9a52-d975a51fb3a9': {'id': 'eea2bcb4-2e1c-412a-9a52-d975a51fb3a9', 'parent': 'e83ec9a7-6b91-4ab1-9dd1-2b2f6ea4d86c', 'children': ['36ba3760-d084-49f6-bce5-fdb2b0d9b748'], 'last_state_change': 1669243477.6124992, 'state': 4, 'task_spec': 'Process_qpfr71f.EndJoin', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '36ba3760-d084-49f6-bce5-fdb2b0d9b748': {'id': '36ba3760-d084-49f6-bce5-fdb2b0d9b748', 'parent': 'eea2bcb4-2e1c-412a-9a52-d975a51fb3a9', 'children': [], 'last_state_change': 1669243477.6125097, 'state': 4, 'task_spec': 'End', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}}, 'root': 'e5f1d75a-8c99-4d01-a3b8-fc6d14996507', 'spec': {'name': 'Process_qpfr71f', 'description': 'MoveBPMNFiles', 'file': 'examples/move_bpmn/move_bpmn.bpmn', 'task_specs': {'Start': {'id': 'Process_qpfr71f_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'Process_qpfr71f.EndJoin': {'id': 'Process_qpfr71f_2', 'name': 'Process_qpfr71f.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_0f7r3q9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'Process_qpfr71f_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Process_qpfr71f.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'Process_qpfr71f_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Activity_0jvfn7c'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 142.0, 'y': 32.0}, 'outgoing_sequence_flows': {'Activity_0jvfn7c': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0my7q5j': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Activity_0jvfn7c': {'id': 'Process_qpfr71f_5', 'name': 'Activity_0jvfn7c', 'description': 'build directory paths', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['Activity_1v124g4'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 90.0}, 'outgoing_sequence_flows': {'Activity_1v124g4': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0vsyo0z': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\nfrom pathlib import Path\n\nhome_dir = str(Path.home())\ndownload_dir = os.path.join(home_dir, "Downloads")\nproject_dir = os.path.join(home_dir, "projects", "github", "jbirddog", "supreme-spoon")', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1v124g4': {'id': 'Process_qpfr71f_6', 'name': 'Activity_1v124g4', 'description': 'find downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0jvfn7c'], 'outputs': ['Activity_1vwbjch'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 200.0}, 'outgoing_sequence_flows': {'Activity_1vwbjch': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_123oz5c': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\ndef is_bpmn_file(filename):\n    return filename.endswith(".bpmn")\n\ndownloaded_bpmn_files = sorted(filter(is_bpmn_file, os.listdir(download_dir)))', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1vwbjch': {'id': 'Process_qpfr71f_7', 'name': 'Activity_1vwbjch', 'description': 'build move source and destinations', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1v124g4'], 'outputs': ['Activity_1onldol'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 310.0}, 'outgoing_sequence_flows': {'Activity_1onldol': {'id': 'Flow_0mo87mc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0mo87mc': {'id': 'Flow_0mo87mc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': '# TODO: look into a dmn table for this\nbpmn_file_destinations = {\n    "move_bpmn.bpmn": "examples/move_bpmn/move_bpmn.bpmn",\n}\n\nunknown_bpmn_files = []\nmove_targets = []\n\nfor bpmn_file in downloaded_bpmn_files:\n    if bpmn_file in bpmn_file_destinations:\n        move_targets.append((bpmn_file, bpmn_file_destinations[bpmn_file]))\n    else:\n        unknown_bpmn_files.append(bpmn_file)', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1onldol': {'id': 'Process_qpfr71f_8', 'name': 'Activity_1onldol', 'description': 'move downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1vwbjch'], 'outputs': ['Event_0f7r3q9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 540.0}, 'outgoing_sequence_flows': {'Event_0f7r3q9': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_05elyac': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\nfor move_target in move_targets:\n    source = os.path.join(download_dir, move_target[0])\n    destination = os.path.join(project_dir, move_target[1])\n    os.replace(source, destination)', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_0f7r3q9': {'id': 'Process_qpfr71f_9', 'name': 'Event_0f7r3q9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1onldol'], 'outputs': ['Process_qpfr71f.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 206.0, 'y': 652.0}, 'outgoing_sequence_flows': {'Process_qpfr71f.EndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_0f7r3q9.ToEndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'Process_qpfr71f_10', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}, 'subprocess_specs': {'Process_qpfr71f': {'name': 'Process_qpfr71f', 'description': 'MoveBPMNFiles', 'file': 'examples/move_bpmn/move_bpmn.bpmn', 'task_specs': {'Start': {'id': 'Process_qpfr71f_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'Process_qpfr71f.EndJoin': {'id': 'Process_qpfr71f_2', 'name': 'Process_qpfr71f.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_0f7r3q9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'Process_qpfr71f_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Process_qpfr71f.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'Process_qpfr71f_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Activity_0jvfn7c'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 142.0, 'y': 32.0}, 'outgoing_sequence_flows': {'Activity_0jvfn7c': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0my7q5j': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Activity_0jvfn7c': {'id': 'Process_qpfr71f_5', 'name': 'Activity_0jvfn7c', 'description': 'build directory paths', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['Activity_1v124g4'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 90.0}, 'outgoing_sequence_flows': {'Activity_1v124g4': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0vsyo0z': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\nfrom pathlib import Path\n\nhome_dir = str(Path.home())\ndownload_dir = os.path.join(home_dir, "Downloads")\nproject_dir = os.path.join(home_dir, "projects", "github", "jbirddog", "supreme-spoon")', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1v124g4': {'id': 'Process_qpfr71f_6', 'name': 'Activity_1v124g4', 'description': 'find downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0jvfn7c'], 'outputs': ['Activity_1vwbjch'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 200.0}, 'outgoing_sequence_flows': {'Activity_1vwbjch': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_123oz5c': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\ndef is_bpmn_file(filename):\n    return filename.endswith(".bpmn")\n\ndownloaded_bpmn_files = sorted(filter(is_bpmn_file, os.listdir(download_dir)))', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1vwbjch': {'id': 'Process_qpfr71f_7', 'name': 'Activity_1vwbjch', 'description': 'build move source and destinations', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1v124g4'], 'outputs': ['Activity_1onldol'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 310.0}, 'outgoing_sequence_flows': {'Activity_1onldol': {'id': 'Flow_0mo87mc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0mo87mc': {'id': 'Flow_0mo87mc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': '# TODO: look into a dmn table for this\nbpmn_file_destinations = {\n    "move_bpmn.bpmn": "examples/move_bpmn/move_bpmn.bpmn",\n}\n\nunknown_bpmn_files = []\nmove_targets = []\n\nfor bpmn_file in downloaded_bpmn_files:\n    if bpmn_file in bpmn_file_destinations:\n        move_targets.append((bpmn_file, bpmn_file_destinations[bpmn_file]))\n    else:\n        unknown_bpmn_files.append(bpmn_file)', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1onldol': {'id': 'Process_qpfr71f_8', 'name': 'Activity_1onldol', 'description': 'move downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1vwbjch'], 'outputs': ['Event_0f7r3q9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 540.0}, 'outgoing_sequence_flows': {'Event_0f7r3q9': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_05elyac': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\nfor move_target in move_targets:\n    source = os.path.join(download_dir, move_target[0])\n    destination = os.path.join(project_dir, move_target[1])\n    os.replace(source, destination)', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_0f7r3q9': {'id': 'Process_qpfr71f_9', 'name': 'Event_0f7r3q9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1onldol'], 'outputs': ['Process_qpfr71f.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 206.0, 'y': 652.0}, 'outgoing_sequence_flows': {'Process_qpfr71f.EndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_0f7r3q9.ToEndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Root': {'id': 'Process_qpfr71f_10', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}}, 'subprocesses': {}, 'bpmn_messages': []}
