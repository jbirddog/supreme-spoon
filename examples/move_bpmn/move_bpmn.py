# GENERATED by Supreme Spoon

from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine
from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter


class MoveBPMNFiles:
    def __init__(self, scripting_additions=None):
        self.scripting_additions = scripting_additions

    def handle_manual_task(instructionsForEndUser=None, description=None, documentation=None):
        def _handler(task):
            print("\nManual Task:\n")
            if description:
                print(f"\t{description.title()}\n")
            if instructionsForEndUser:
                print(f"\t{instructionsForEndUser}\n")
            if documentation:
                print(f"\t{documentation}\n")
            input("Press enter to continue")
        return _handler

    TASK_HANDLERS = {
        "Activity_1f00v7w": handle_manual_task(**{'instructionsForEndUser': 'Saw unknown bpmn files. Confirm deletion or quit the process to abort.', 'description': 'confirm unknown bpmn file deletion'}),

    }

    def get_serializer(self):
        spec_converters = [ManualTaskConverter, ScriptTaskConverter]
        spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(spec_converters)
        serializer = BpmnWorkflowSerializer(spec_converter, version="1.0-supreme-spoon")
        return serializer

    # TODO: restore
    def get_workflow(self):
        workflow = self.get_serializer().workflow_from_dict(self.SERIALIZED_WORKFLOW)

        if self.scripting_additions is not None:
            workflow.script_engine = PythonScriptEngine(scripting_additions=self.scripting_additions)

        return workflow

    def run(self):
        workflow = self.get_workflow()
        workflow.do_engine_steps()
        while not workflow.is_completed():
            ready_tasks = workflow.get_ready_user_tasks()
            for task in ready_tasks:
                if task.task_spec.name in self.TASK_HANDLERS:
                    self.TASK_HANDLERS[task.task_spec.name](task)
                task.complete()
            workflow.refresh_waiting_tasks()
            workflow.do_engine_steps()

        return workflow.data

    SERIALIZED_WORKFLOW = {'data': {}, 'last_task': None, 'success': True, 'tasks': {'e2daf0e7-75b6-4a2a-838c-eb9996cb7b8c': {'id': 'e2daf0e7-75b6-4a2a-838c-eb9996cb7b8c', 'parent': None, 'children': ['58122f7d-6903-43d2-9bfe-45532f111021'], 'last_state_change': 1669255193.794006, 'state': 32, 'task_spec': 'Root', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '58122f7d-6903-43d2-9bfe-45532f111021': {'id': '58122f7d-6903-43d2-9bfe-45532f111021', 'parent': 'e2daf0e7-75b6-4a2a-838c-eb9996cb7b8c', 'children': ['b7af1e5a-22f7-410c-ac88-82c003faffa2'], 'last_state_change': 1669255193.7941906, 'state': 16, 'task_spec': 'Start', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'b7af1e5a-22f7-410c-ac88-82c003faffa2': {'id': 'b7af1e5a-22f7-410c-ac88-82c003faffa2', 'parent': '58122f7d-6903-43d2-9bfe-45532f111021', 'children': ['40b29105-ed33-4d55-9c6d-b546b84be24b'], 'last_state_change': 1669255193.794033, 'state': 4, 'task_spec': 'StartEvent_1', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '40b29105-ed33-4d55-9c6d-b546b84be24b': {'id': '40b29105-ed33-4d55-9c6d-b546b84be24b', 'parent': 'b7af1e5a-22f7-410c-ac88-82c003faffa2', 'children': ['b1c819ba-2346-49d9-b3ce-a7303a3d5bfa'], 'last_state_change': 1669255193.7940488, 'state': 4, 'task_spec': 'Activity_0jvfn7c', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'b1c819ba-2346-49d9-b3ce-a7303a3d5bfa': {'id': 'b1c819ba-2346-49d9-b3ce-a7303a3d5bfa', 'parent': '40b29105-ed33-4d55-9c6d-b546b84be24b', 'children': ['14632638-4871-4b08-b619-45915b58308b'], 'last_state_change': 1669255193.794063, 'state': 4, 'task_spec': 'Activity_1v124g4', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '14632638-4871-4b08-b619-45915b58308b': {'id': '14632638-4871-4b08-b619-45915b58308b', 'parent': 'b1c819ba-2346-49d9-b3ce-a7303a3d5bfa', 'children': ['b3a9c9eb-c179-4487-bfbf-291e26f04104'], 'last_state_change': 1669255193.7940736, 'state': 4, 'task_spec': 'Activity_1vwbjch', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'b3a9c9eb-c179-4487-bfbf-291e26f04104': {'id': 'b3a9c9eb-c179-4487-bfbf-291e26f04104', 'parent': '14632638-4871-4b08-b619-45915b58308b', 'children': ['43536a70-1de9-4c7b-a31d-484325a563dd', 'fd596260-8097-415a-ab2c-80e8a8732b1a'], 'last_state_change': 1669255193.7940843, 'state': 4, 'task_spec': 'Gateway_1fnsa3q', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '43536a70-1de9-4c7b-a31d-484325a563dd': {'id': '43536a70-1de9-4c7b-a31d-484325a563dd', 'parent': 'b3a9c9eb-c179-4487-bfbf-291e26f04104', 'children': ['66256fdf-64ba-4392-87c3-3d2c7b4c6187'], 'last_state_change': 1669255193.7940977, 'state': 1, 'task_spec': 'Activity_1f00v7w', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '66256fdf-64ba-4392-87c3-3d2c7b4c6187': {'id': '66256fdf-64ba-4392-87c3-3d2c7b4c6187', 'parent': '43536a70-1de9-4c7b-a31d-484325a563dd', 'children': [], 'last_state_change': 1669255193.7941177, 'state': 1, 'task_spec': 'Activity_199a27l', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, 'fd596260-8097-415a-ab2c-80e8a8732b1a': {'id': 'fd596260-8097-415a-ab2c-80e8a8732b1a', 'parent': 'b3a9c9eb-c179-4487-bfbf-291e26f04104', 'children': ['02468480-324d-4c39-893a-6dcdcb428e62'], 'last_state_change': 1669255193.7941053, 'state': 1, 'task_spec': 'Activity_1onldol', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}, '02468480-324d-4c39-893a-6dcdcb428e62': {'id': '02468480-324d-4c39-893a-6dcdcb428e62', 'parent': 'fd596260-8097-415a-ab2c-80e8a8732b1a', 'children': [], 'last_state_change': 1669255193.7941387, 'state': 1, 'task_spec': 'Event_0f7r3q9', 'triggered': False, 'workflow_name': 'Process_qpfr71f', 'internal_data': {}, 'data': {}}}, 'root': 'e2daf0e7-75b6-4a2a-838c-eb9996cb7b8c', 'spec': {'name': 'Process_qpfr71f', 'description': 'MoveBPMNFiles', 'file': 'examples/move_bpmn/move_bpmn.bpmn', 'task_specs': {'Start': {'id': 'Process_qpfr71f_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'Process_qpfr71f.EndJoin': {'id': 'Process_qpfr71f_2', 'name': 'Process_qpfr71f.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_0f7r3q9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'Process_qpfr71f_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Process_qpfr71f.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'Process_qpfr71f_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Activity_0jvfn7c'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 142.0, 'y': 32.0}, 'outgoing_sequence_flows': {'Activity_0jvfn7c': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0my7q5j': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Activity_0jvfn7c': {'id': 'Process_qpfr71f_5', 'name': 'Activity_0jvfn7c', 'description': 'build directory paths', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['Activity_1v124g4'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 90.0}, 'outgoing_sequence_flows': {'Activity_1v124g4': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0vsyo0z': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\nfrom pathlib import Path\n\nhome_dir = str(Path.home())\ndownload_dir = os.path.join(home_dir, "Downloads")\nproject_dir = os.path.join(home_dir, "projects", "github", "jbirddog", "supreme-spoon")', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1v124g4': {'id': 'Process_qpfr71f_6', 'name': 'Activity_1v124g4', 'description': 'find downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0jvfn7c'], 'outputs': ['Activity_1vwbjch'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 200.0}, 'outgoing_sequence_flows': {'Activity_1vwbjch': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_123oz5c': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\ndef is_bpmn_file(filename):\n    return filename.endswith(".bpmn")\n\ndownloaded_bpmn_files = sorted(filter(is_bpmn_file, os.listdir(download_dir)))', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1vwbjch': {'id': 'Process_qpfr71f_7', 'name': 'Activity_1vwbjch', 'description': 'build move source and destinations', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1v124g4'], 'outputs': ['Gateway_1fnsa3q'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 310.0}, 'outgoing_sequence_flows': {'Gateway_1fnsa3q': {'id': 'Flow_1hr87gn', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_1fnsa3q', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1hr87gn': {'id': 'Flow_1hr87gn', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_1fnsa3q', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': '# TODO: look into a dmn table for this\nbpmn_file_destinations = {\n    "move_bpmn.bpmn": "examples/move_bpmn/move_bpmn.bpmn",\n}\n\nunknown_bpmn_files = []\nmove_targets = []\n\nfor bpmn_file in downloaded_bpmn_files:\n    if bpmn_file in bpmn_file_destinations:\n        move_targets.append((bpmn_file, bpmn_file_destinations[bpmn_file]))\n    else:\n        unknown_bpmn_files.append(bpmn_file)\n\nsaw_unknown_bpmn_files = len(unknown_bpmn_files) > 0', 'typename': 'ScriptTask', 'extensions': {}}, 'Gateway_1fnsa3q': {'id': 'Process_qpfr71f_8', 'name': 'Gateway_1fnsa3q', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1vwbjch'], 'outputs': ['Activity_1f00v7w', 'Activity_1onldol'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 199.0, 'y': 425.0}, 'outgoing_sequence_flows': {'Activity_1f00v7w': {'id': 'Flow_16aapr5', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1f00v7w', 'typename': 'SequenceFlow'}, 'Activity_1onldol': {'id': 'Flow_1yte886', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_16aapr5': {'id': 'Flow_16aapr5', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1f00v7w', 'typename': 'SequenceFlow'}, 'Flow_1yte886': {'id': 'Flow_1yte886', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'default_task_spec': None, 'cond_task_specs': [{'condition': 'saw_unknown_bpmn_files == True', 'task_spec': 'Activity_1f00v7w'}, {'condition': 'saw_unknown_bpmn_files == False', 'task_spec': 'Activity_1onldol'}], 'choice': None, 'typename': 'ExclusiveGateway', 'extensions': {}}, 'Activity_1onldol': {'id': 'Process_qpfr71f_9', 'name': 'Activity_1onldol', 'description': 'move downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_199a27l', 'Gateway_1fnsa3q'], 'outputs': ['Event_0f7r3q9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 540.0}, 'outgoing_sequence_flows': {'Event_0f7r3q9': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_05elyac': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\nfor move_target in move_targets:\n    source = os.path.join(download_dir, move_target[0])\n    destination = os.path.join(project_dir, move_target[1])\n    os.replace(source, destination)', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_0f7r3q9': {'id': 'Process_qpfr71f_10', 'name': 'Event_0f7r3q9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1onldol'], 'outputs': ['Process_qpfr71f.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 206.0, 'y': 652.0}, 'outgoing_sequence_flows': {'Process_qpfr71f.EndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_0f7r3q9.ToEndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Activity_1f00v7w': {'id': 'Process_qpfr71f_11', 'name': 'Activity_1f00v7w', 'description': 'confirm unknown bpmn file deletion', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_1fnsa3q'], 'outputs': ['Activity_199a27l'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 410.0}, 'outgoing_sequence_flows': {'Activity_199a27l': {'id': 'Flow_0nopkgo', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_199a27l', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0nopkgo': {'id': 'Flow_0nopkgo', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_199a27l', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'typename': 'ManualTask', 'extensions': {'instructionsForEndUser': 'Saw unknown bpmn files. Confirm deletion or quit the process to abort.', 'description': 'confirm unknown bpmn file deletion'}}, 'Activity_199a27l': {'id': 'Process_qpfr71f_12', 'name': 'Activity_199a27l', 'description': 'delete unknow bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1f00v7w'], 'outputs': ['Activity_1onldol'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 440.0, 'y': 410.0}, 'outgoing_sequence_flows': {'Activity_1onldol': {'id': 'Flow_1xsxefe', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1xsxefe': {'id': 'Flow_1xsxefe', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\nfor unknown_bpmn_file in unknown_bpmn_files:\n    os.remove(os.path.join(download_dir, unknown_bpmn_file))', 'typename': 'ScriptTask', 'extensions': {}}, 'Root': {'id': 'Process_qpfr71f_13', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}, 'subprocess_specs': {'Process_qpfr71f': {'name': 'Process_qpfr71f', 'description': 'MoveBPMNFiles', 'file': 'examples/move_bpmn/move_bpmn.bpmn', 'task_specs': {'Start': {'id': 'Process_qpfr71f_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['StartEvent_1'], 'typename': 'StartTask'}, 'Process_qpfr71f.EndJoin': {'id': 'Process_qpfr71f_2', 'name': 'Process_qpfr71f.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_0f7r3q9'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'Process_qpfr71f_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Process_qpfr71f.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'StartEvent_1': {'id': 'Process_qpfr71f_4', 'name': 'StartEvent_1', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Activity_0jvfn7c'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 142.0, 'y': 32.0}, 'outgoing_sequence_flows': {'Activity_0jvfn7c': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0my7q5j': {'id': 'Flow_0my7q5j', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0jvfn7c', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Activity_0jvfn7c': {'id': 'Process_qpfr71f_5', 'name': 'Activity_0jvfn7c', 'description': 'build directory paths', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['StartEvent_1'], 'outputs': ['Activity_1v124g4'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 90.0}, 'outgoing_sequence_flows': {'Activity_1v124g4': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0vsyo0z': {'id': 'Flow_0vsyo0z', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1v124g4', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\nfrom pathlib import Path\n\nhome_dir = str(Path.home())\ndownload_dir = os.path.join(home_dir, "Downloads")\nproject_dir = os.path.join(home_dir, "projects", "github", "jbirddog", "supreme-spoon")', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1v124g4': {'id': 'Process_qpfr71f_6', 'name': 'Activity_1v124g4', 'description': 'find downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0jvfn7c'], 'outputs': ['Activity_1vwbjch'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 200.0}, 'outgoing_sequence_flows': {'Activity_1vwbjch': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_123oz5c': {'id': 'Flow_123oz5c', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1vwbjch', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\ndef is_bpmn_file(filename):\n    return filename.endswith(".bpmn")\n\ndownloaded_bpmn_files = sorted(filter(is_bpmn_file, os.listdir(download_dir)))', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1vwbjch': {'id': 'Process_qpfr71f_7', 'name': 'Activity_1vwbjch', 'description': 'build move source and destinations', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1v124g4'], 'outputs': ['Gateway_1fnsa3q'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 310.0}, 'outgoing_sequence_flows': {'Gateway_1fnsa3q': {'id': 'Flow_1hr87gn', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_1fnsa3q', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1hr87gn': {'id': 'Flow_1hr87gn', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_1fnsa3q', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': '# TODO: look into a dmn table for this\nbpmn_file_destinations = {\n    "move_bpmn.bpmn": "examples/move_bpmn/move_bpmn.bpmn",\n}\n\nunknown_bpmn_files = []\nmove_targets = []\n\nfor bpmn_file in downloaded_bpmn_files:\n    if bpmn_file in bpmn_file_destinations:\n        move_targets.append((bpmn_file, bpmn_file_destinations[bpmn_file]))\n    else:\n        unknown_bpmn_files.append(bpmn_file)\n\nsaw_unknown_bpmn_files = len(unknown_bpmn_files) > 0', 'typename': 'ScriptTask', 'extensions': {}}, 'Gateway_1fnsa3q': {'id': 'Process_qpfr71f_8', 'name': 'Gateway_1fnsa3q', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1vwbjch'], 'outputs': ['Activity_1f00v7w', 'Activity_1onldol'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 199.0, 'y': 425.0}, 'outgoing_sequence_flows': {'Activity_1f00v7w': {'id': 'Flow_16aapr5', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1f00v7w', 'typename': 'SequenceFlow'}, 'Activity_1onldol': {'id': 'Flow_1yte886', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_16aapr5': {'id': 'Flow_16aapr5', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1f00v7w', 'typename': 'SequenceFlow'}, 'Flow_1yte886': {'id': 'Flow_1yte886', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'default_task_spec': None, 'cond_task_specs': [{'condition': 'saw_unknown_bpmn_files == True', 'task_spec': 'Activity_1f00v7w'}, {'condition': 'saw_unknown_bpmn_files == False', 'task_spec': 'Activity_1onldol'}], 'choice': None, 'typename': 'ExclusiveGateway', 'extensions': {}}, 'Activity_1onldol': {'id': 'Process_qpfr71f_9', 'name': 'Activity_1onldol', 'description': 'move downloaded bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_199a27l', 'Gateway_1fnsa3q'], 'outputs': ['Event_0f7r3q9'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 174.0, 'y': 540.0}, 'outgoing_sequence_flows': {'Event_0f7r3q9': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_05elyac': {'id': 'Flow_05elyac', 'name': None, 'documentation': None, 'target_task_spec': 'Event_0f7r3q9', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\nfor move_target in move_targets:\n    source = os.path.join(download_dir, move_target[0])\n    destination = os.path.join(project_dir, move_target[1])\n    os.replace(source, destination)', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_0f7r3q9': {'id': 'Process_qpfr71f_10', 'name': 'Event_0f7r3q9', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1onldol'], 'outputs': ['Process_qpfr71f.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 206.0, 'y': 652.0}, 'outgoing_sequence_flows': {'Process_qpfr71f.EndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_0f7r3q9.ToEndJoin': {'id': 'Event_0f7r3q9.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'Process_qpfr71f.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Activity_1f00v7w': {'id': 'Process_qpfr71f_11', 'name': 'Activity_1f00v7w', 'description': 'confirm unknown bpmn file deletion', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_1fnsa3q'], 'outputs': ['Activity_199a27l'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 410.0}, 'outgoing_sequence_flows': {'Activity_199a27l': {'id': 'Flow_0nopkgo', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_199a27l', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0nopkgo': {'id': 'Flow_0nopkgo', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_199a27l', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'typename': 'ManualTask', 'extensions': {'instructionsForEndUser': 'Saw unknown bpmn files. Confirm deletion or quit the process to abort.', 'description': 'confirm unknown bpmn file deletion'}}, 'Activity_199a27l': {'id': 'Process_qpfr71f_12', 'name': 'Activity_199a27l', 'description': 'delete unknow bpmn files', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1f00v7w'], 'outputs': ['Activity_1onldol'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 440.0, 'y': 410.0}, 'outgoing_sequence_flows': {'Activity_1onldol': {'id': 'Flow_1xsxefe', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1xsxefe': {'id': 'Flow_1xsxefe', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1onldol', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'import os\n\nfor unknown_bpmn_file in unknown_bpmn_files:\n    os.remove(os.path.join(download_dir, unknown_bpmn_file))', 'typename': 'ScriptTask', 'extensions': {}}, 'Root': {'id': 'Process_qpfr71f_13', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}}, 'subprocesses': {}, 'bpmn_messages': []}
