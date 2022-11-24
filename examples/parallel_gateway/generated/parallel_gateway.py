# GENERATED by Supreme Spoon

from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine
from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter


class ParallelGatewayWorkflow:
    def __init__(self, scripting_additions=None):
        self.scripting_additions = scripting_additions

    def get_serializer(self):
        spec_converters = [ScriptTaskConverter]
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

    SERIALIZED_WORKFLOW = {'data': {}, 'last_task': None, 'success': True, 'tasks': {'dde236e5-6566-466c-a439-aea1dcd85b63': {'id': 'dde236e5-6566-466c-a439-aea1dcd85b63', 'parent': None, 'children': ['994b6157-f34e-44dc-9a61-cfe17fa156d2'], 'last_state_change': 1669258974.471907, 'state': 32, 'task_spec': 'Root', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '994b6157-f34e-44dc-9a61-cfe17fa156d2': {'id': '994b6157-f34e-44dc-9a61-cfe17fa156d2', 'parent': 'dde236e5-6566-466c-a439-aea1dcd85b63', 'children': ['25aaa06f-8d22-4bc6-9bfe-96d26d05b8c1'], 'last_state_change': 1669258974.4721923, 'state': 16, 'task_spec': 'Start', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '25aaa06f-8d22-4bc6-9bfe-96d26d05b8c1': {'id': '25aaa06f-8d22-4bc6-9bfe-96d26d05b8c1', 'parent': '994b6157-f34e-44dc-9a61-cfe17fa156d2', 'children': ['b2c34e14-612b-4c57-8d8e-c9b028a9ea4f'], 'last_state_change': 1669258974.4719326, 'state': 4, 'task_spec': 'Event_056euq0', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'b2c34e14-612b-4c57-8d8e-c9b028a9ea4f': {'id': 'b2c34e14-612b-4c57-8d8e-c9b028a9ea4f', 'parent': '25aaa06f-8d22-4bc6-9bfe-96d26d05b8c1', 'children': ['99791dd0-4882-45ae-b4c2-ff693ec20186', '88fa0584-08e3-418b-aa87-24070dcb95a9', '81f94929-bfd8-4d6f-885d-97f0d8ad8228'], 'last_state_change': 1669258974.4719505, 'state': 4, 'task_spec': 'Gateway_017jnp6', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '99791dd0-4882-45ae-b4c2-ff693ec20186': {'id': '99791dd0-4882-45ae-b4c2-ff693ec20186', 'parent': 'b2c34e14-612b-4c57-8d8e-c9b028a9ea4f', 'children': ['923aed8e-cacc-40d8-9ffd-9e4fdb61f198'], 'last_state_change': 1669258974.4719663, 'state': 4, 'task_spec': 'Activity_1ewv0kb', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '923aed8e-cacc-40d8-9ffd-9e4fdb61f198': {'id': '923aed8e-cacc-40d8-9ffd-9e4fdb61f198', 'parent': '99791dd0-4882-45ae-b4c2-ff693ec20186', 'children': ['f66bf616-a708-436a-8903-804802e7ff19'], 'last_state_change': 1669258974.4719946, 'state': 4, 'task_spec': 'Gateway_0chrwmq', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'f66bf616-a708-436a-8903-804802e7ff19': {'id': 'f66bf616-a708-436a-8903-804802e7ff19', 'parent': '923aed8e-cacc-40d8-9ffd-9e4fdb61f198', 'children': ['e4cd0cc5-38ad-4b2e-a089-6df2c685b6e1'], 'last_state_change': 1669258974.4720058, 'state': 4, 'task_spec': 'Activity_0kapn49', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'e4cd0cc5-38ad-4b2e-a089-6df2c685b6e1': {'id': 'e4cd0cc5-38ad-4b2e-a089-6df2c685b6e1', 'parent': 'f66bf616-a708-436a-8903-804802e7ff19', 'children': ['1d1de666-b4db-4c91-8a81-8f952099617c'], 'last_state_change': 1669258974.4720151, 'state': 4, 'task_spec': 'Event_1kj6hcj', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '1d1de666-b4db-4c91-8a81-8f952099617c': {'id': '1d1de666-b4db-4c91-8a81-8f952099617c', 'parent': 'e4cd0cc5-38ad-4b2e-a089-6df2c685b6e1', 'children': ['b68c84ec-4ad6-4e31-a4ed-67094f5cc558'], 'last_state_change': 1669258974.4720237, 'state': 4, 'task_spec': 'ParallelGatewayWorkflow.EndJoin', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'b68c84ec-4ad6-4e31-a4ed-67094f5cc558': {'id': 'b68c84ec-4ad6-4e31-a4ed-67094f5cc558', 'parent': '1d1de666-b4db-4c91-8a81-8f952099617c', 'children': [], 'last_state_change': 1669258974.4720333, 'state': 4, 'task_spec': 'End', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '88fa0584-08e3-418b-aa87-24070dcb95a9': {'id': '88fa0584-08e3-418b-aa87-24070dcb95a9', 'parent': 'b2c34e14-612b-4c57-8d8e-c9b028a9ea4f', 'children': ['ac6989ce-7c5a-4a97-afb1-634e602b81e6'], 'last_state_change': 1669258974.4719727, 'state': 4, 'task_spec': 'Activity_115woll', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'ac6989ce-7c5a-4a97-afb1-634e602b81e6': {'id': 'ac6989ce-7c5a-4a97-afb1-634e602b81e6', 'parent': '88fa0584-08e3-418b-aa87-24070dcb95a9', 'children': ['6c34706f-7cd4-4655-8c67-dd5739e20240'], 'last_state_change': 1669258974.4720445, 'state': 4, 'task_spec': 'Gateway_0chrwmq', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '6c34706f-7cd4-4655-8c67-dd5739e20240': {'id': '6c34706f-7cd4-4655-8c67-dd5739e20240', 'parent': 'ac6989ce-7c5a-4a97-afb1-634e602b81e6', 'children': ['39386093-a141-40e6-a543-3517beee431d'], 'last_state_change': 1669258974.4720528, 'state': 4, 'task_spec': 'Activity_0kapn49', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '39386093-a141-40e6-a543-3517beee431d': {'id': '39386093-a141-40e6-a543-3517beee431d', 'parent': '6c34706f-7cd4-4655-8c67-dd5739e20240', 'children': ['e3fda9ca-1ab3-4579-b257-fec81d97339d'], 'last_state_change': 1669258974.472061, 'state': 4, 'task_spec': 'Event_1kj6hcj', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'e3fda9ca-1ab3-4579-b257-fec81d97339d': {'id': 'e3fda9ca-1ab3-4579-b257-fec81d97339d', 'parent': '39386093-a141-40e6-a543-3517beee431d', 'children': ['cf9155e8-e26a-4c22-9af4-bc95dbaab602'], 'last_state_change': 1669258974.4720685, 'state': 4, 'task_spec': 'ParallelGatewayWorkflow.EndJoin', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'cf9155e8-e26a-4c22-9af4-bc95dbaab602': {'id': 'cf9155e8-e26a-4c22-9af4-bc95dbaab602', 'parent': 'e3fda9ca-1ab3-4579-b257-fec81d97339d', 'children': [], 'last_state_change': 1669258974.4720774, 'state': 4, 'task_spec': 'End', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '81f94929-bfd8-4d6f-885d-97f0d8ad8228': {'id': '81f94929-bfd8-4d6f-885d-97f0d8ad8228', 'parent': 'b2c34e14-612b-4c57-8d8e-c9b028a9ea4f', 'children': ['4e362bc6-e7f3-4935-979b-4ce99dc8895e'], 'last_state_change': 1669258974.4719787, 'state': 4, 'task_spec': 'Activity_1g1cdox', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '4e362bc6-e7f3-4935-979b-4ce99dc8895e': {'id': '4e362bc6-e7f3-4935-979b-4ce99dc8895e', 'parent': '81f94929-bfd8-4d6f-885d-97f0d8ad8228', 'children': ['c20db7d3-5072-40d9-b260-11451cbbac8a'], 'last_state_change': 1669258974.4720871, 'state': 4, 'task_spec': 'Gateway_0chrwmq', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'c20db7d3-5072-40d9-b260-11451cbbac8a': {'id': 'c20db7d3-5072-40d9-b260-11451cbbac8a', 'parent': '4e362bc6-e7f3-4935-979b-4ce99dc8895e', 'children': ['a75b7d12-78a1-411c-8142-ad9d287db88f'], 'last_state_change': 1669258974.4720948, 'state': 4, 'task_spec': 'Activity_0kapn49', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'a75b7d12-78a1-411c-8142-ad9d287db88f': {'id': 'a75b7d12-78a1-411c-8142-ad9d287db88f', 'parent': 'c20db7d3-5072-40d9-b260-11451cbbac8a', 'children': ['9a93eb26-1e40-4034-b8ab-9926ad15c74b'], 'last_state_change': 1669258974.472102, 'state': 4, 'task_spec': 'Event_1kj6hcj', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, '9a93eb26-1e40-4034-b8ab-9926ad15c74b': {'id': '9a93eb26-1e40-4034-b8ab-9926ad15c74b', 'parent': 'a75b7d12-78a1-411c-8142-ad9d287db88f', 'children': ['f28cfe5b-fb2c-488a-8c01-d6df07fadf72'], 'last_state_change': 1669258974.4721098, 'state': 4, 'task_spec': 'ParallelGatewayWorkflow.EndJoin', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}, 'f28cfe5b-fb2c-488a-8c01-d6df07fadf72': {'id': 'f28cfe5b-fb2c-488a-8c01-d6df07fadf72', 'parent': '9a93eb26-1e40-4034-b8ab-9926ad15c74b', 'children': [], 'last_state_change': 1669258974.4721174, 'state': 4, 'task_spec': 'End', 'triggered': False, 'workflow_name': 'ParallelGatewayWorkflow', 'internal_data': {}, 'data': {}}}, 'root': 'dde236e5-6566-466c-a439-aea1dcd85b63', 'spec': {'name': 'ParallelGatewayWorkflow', 'description': 'ParallelGatewayWorkflow', 'file': 'examples/parallel_gateway/bpmn/parallel_gateway.bpmn', 'task_specs': {'Start': {'id': 'ParallelGatewayWorkflow_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['Event_056euq0'], 'typename': 'StartTask'}, 'ParallelGatewayWorkflow.EndJoin': {'id': 'ParallelGatewayWorkflow_2', 'name': 'ParallelGatewayWorkflow.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_1kj6hcj'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'ParallelGatewayWorkflow_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['ParallelGatewayWorkflow.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'Event_056euq0': {'id': 'ParallelGatewayWorkflow_4', 'name': 'Event_056euq0', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Gateway_017jnp6'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 142.0, 'y': 162.0}, 'outgoing_sequence_flows': {'Gateway_017jnp6': {'id': 'Flow_1cl1p98', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_017jnp6', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1cl1p98': {'id': 'Flow_1cl1p98', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_017jnp6', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Gateway_017jnp6': {'id': 'ParallelGatewayWorkflow_5', 'name': 'Gateway_017jnp6', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_056euq0'], 'outputs': ['Activity_1ewv0kb', 'Activity_115woll', 'Activity_1g1cdox'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 205.0, 'y': 155.0}, 'outgoing_sequence_flows': {'Activity_1ewv0kb': {'id': 'Flow_1pitxjc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1ewv0kb', 'typename': 'SequenceFlow'}, 'Activity_115woll': {'id': 'Flow_0h2b3iu', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_115woll', 'typename': 'SequenceFlow'}, 'Activity_1g1cdox': {'id': 'Flow_02o1fhb', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1g1cdox', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1pitxjc': {'id': 'Flow_1pitxjc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1ewv0kb', 'typename': 'SequenceFlow'}, 'Flow_0h2b3iu': {'id': 'Flow_0h2b3iu', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_115woll', 'typename': 'SequenceFlow'}, 'Flow_02o1fhb': {'id': 'Flow_02o1fhb', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1g1cdox', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'split_task': None, 'threshold': None, 'cancel': False, 'typename': 'ParallelGateway', 'extensions': {}}, 'Activity_1ewv0kb': {'id': 'ParallelGatewayWorkflow_6', 'name': 'Activity_1ewv0kb', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_017jnp6'], 'outputs': ['Gateway_0chrwmq'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 30.0}, 'outgoing_sequence_flows': {'Gateway_0chrwmq': {'id': 'Flow_0iqfly5', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0iqfly5': {'id': 'Flow_0iqfly5', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'var1=4', 'typename': 'ScriptTask', 'extensions': {}}, 'Gateway_0chrwmq': {'id': 'ParallelGatewayWorkflow_7', 'name': 'Gateway_0chrwmq', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1ewv0kb', 'Activity_115woll', 'Activity_1g1cdox'], 'outputs': ['Activity_0kapn49'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 445.0, 'y': 155.0}, 'outgoing_sequence_flows': {'Activity_0kapn49': {'id': 'Flow_19o9wjn', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0kapn49', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_19o9wjn': {'id': 'Flow_19o9wjn', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0kapn49', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'split_task': None, 'threshold': None, 'cancel': False, 'typename': 'ParallelGateway', 'extensions': {}}, 'Activity_0kapn49': {'id': 'ParallelGatewayWorkflow_8', 'name': 'Activity_0kapn49', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_0chrwmq'], 'outputs': ['Event_1kj6hcj'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 590.0, 'y': 140.0}, 'outgoing_sequence_flows': {'Event_1kj6hcj': {'id': 'Flow_0xt37g5', 'name': None, 'documentation': None, 'target_task_spec': 'Event_1kj6hcj', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0xt37g5': {'id': 'Flow_0xt37g5', 'name': None, 'documentation': None, 'target_task_spec': 'Event_1kj6hcj', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'result = var1 + 3', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_1kj6hcj': {'id': 'ParallelGatewayWorkflow_9', 'name': 'Event_1kj6hcj', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0kapn49'], 'outputs': ['ParallelGatewayWorkflow.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 792.0, 'y': 162.0}, 'outgoing_sequence_flows': {'ParallelGatewayWorkflow.EndJoin': {'id': 'Event_1kj6hcj.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'ParallelGatewayWorkflow.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_1kj6hcj.ToEndJoin': {'id': 'Event_1kj6hcj.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'ParallelGatewayWorkflow.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Activity_115woll': {'id': 'ParallelGatewayWorkflow_10', 'name': 'Activity_115woll', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_017jnp6'], 'outputs': ['Gateway_0chrwmq'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 140.0}, 'outgoing_sequence_flows': {'Gateway_0chrwmq': {'id': 'Flow_1iiolp4', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1iiolp4': {'id': 'Flow_1iiolp4', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'var1=6', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1g1cdox': {'id': 'ParallelGatewayWorkflow_11', 'name': 'Activity_1g1cdox', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_017jnp6'], 'outputs': ['Gateway_0chrwmq'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 250.0}, 'outgoing_sequence_flows': {'Gateway_0chrwmq': {'id': 'Flow_110tzrd', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_110tzrd': {'id': 'Flow_110tzrd', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'var1=7', 'typename': 'ScriptTask', 'extensions': {}}, 'Root': {'id': 'ParallelGatewayWorkflow_12', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}, 'subprocess_specs': {'ParallelGatewayWorkflow': {'name': 'ParallelGatewayWorkflow', 'description': 'ParallelGatewayWorkflow', 'file': 'examples/parallel_gateway/bpmn/parallel_gateway.bpmn', 'task_specs': {'Start': {'id': 'ParallelGatewayWorkflow_1', 'name': 'Start', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': ['Event_056euq0'], 'typename': 'StartTask'}, 'ParallelGatewayWorkflow.EndJoin': {'id': 'ParallelGatewayWorkflow_2', 'name': 'ParallelGatewayWorkflow.EndJoin', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_1kj6hcj'], 'outputs': ['End'], 'typename': '_EndJoin'}, 'End': {'id': 'ParallelGatewayWorkflow_3', 'name': 'End', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['ParallelGatewayWorkflow.EndJoin'], 'outputs': [], 'typename': 'Simple'}, 'Event_056euq0': {'id': 'ParallelGatewayWorkflow_4', 'name': 'Event_056euq0', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Start'], 'outputs': ['Gateway_017jnp6'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 142.0, 'y': 162.0}, 'outgoing_sequence_flows': {'Gateway_017jnp6': {'id': 'Flow_1cl1p98', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_017jnp6', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1cl1p98': {'id': 'Flow_1cl1p98', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_017jnp6', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'StartEvent', 'extensions': {}}, 'Gateway_017jnp6': {'id': 'ParallelGatewayWorkflow_5', 'name': 'Gateway_017jnp6', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Event_056euq0'], 'outputs': ['Activity_1ewv0kb', 'Activity_115woll', 'Activity_1g1cdox'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 205.0, 'y': 155.0}, 'outgoing_sequence_flows': {'Activity_1ewv0kb': {'id': 'Flow_1pitxjc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1ewv0kb', 'typename': 'SequenceFlow'}, 'Activity_115woll': {'id': 'Flow_0h2b3iu', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_115woll', 'typename': 'SequenceFlow'}, 'Activity_1g1cdox': {'id': 'Flow_02o1fhb', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1g1cdox', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1pitxjc': {'id': 'Flow_1pitxjc', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1ewv0kb', 'typename': 'SequenceFlow'}, 'Flow_0h2b3iu': {'id': 'Flow_0h2b3iu', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_115woll', 'typename': 'SequenceFlow'}, 'Flow_02o1fhb': {'id': 'Flow_02o1fhb', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_1g1cdox', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'split_task': None, 'threshold': None, 'cancel': False, 'typename': 'ParallelGateway', 'extensions': {}}, 'Activity_1ewv0kb': {'id': 'ParallelGatewayWorkflow_6', 'name': 'Activity_1ewv0kb', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_017jnp6'], 'outputs': ['Gateway_0chrwmq'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 30.0}, 'outgoing_sequence_flows': {'Gateway_0chrwmq': {'id': 'Flow_0iqfly5', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0iqfly5': {'id': 'Flow_0iqfly5', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'var1=4', 'typename': 'ScriptTask', 'extensions': {}}, 'Gateway_0chrwmq': {'id': 'ParallelGatewayWorkflow_7', 'name': 'Gateway_0chrwmq', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_1ewv0kb', 'Activity_115woll', 'Activity_1g1cdox'], 'outputs': ['Activity_0kapn49'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 445.0, 'y': 155.0}, 'outgoing_sequence_flows': {'Activity_0kapn49': {'id': 'Flow_19o9wjn', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0kapn49', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_19o9wjn': {'id': 'Flow_19o9wjn', 'name': None, 'documentation': None, 'target_task_spec': 'Activity_0kapn49', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'split_task': None, 'threshold': None, 'cancel': False, 'typename': 'ParallelGateway', 'extensions': {}}, 'Activity_0kapn49': {'id': 'ParallelGatewayWorkflow_8', 'name': 'Activity_0kapn49', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_0chrwmq'], 'outputs': ['Event_1kj6hcj'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 590.0, 'y': 140.0}, 'outgoing_sequence_flows': {'Event_1kj6hcj': {'id': 'Flow_0xt37g5', 'name': None, 'documentation': None, 'target_task_spec': 'Event_1kj6hcj', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_0xt37g5': {'id': 'Flow_0xt37g5', 'name': None, 'documentation': None, 'target_task_spec': 'Event_1kj6hcj', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'result = var1 + 3', 'typename': 'ScriptTask', 'extensions': {}}, 'Event_1kj6hcj': {'id': 'ParallelGatewayWorkflow_9', 'name': 'Event_1kj6hcj', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Activity_0kapn49'], 'outputs': ['ParallelGatewayWorkflow.EndJoin'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 792.0, 'y': 162.0}, 'outgoing_sequence_flows': {'ParallelGatewayWorkflow.EndJoin': {'id': 'Event_1kj6hcj.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'ParallelGatewayWorkflow.EndJoin', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Event_1kj6hcj.ToEndJoin': {'id': 'Event_1kj6hcj.ToEndJoin', 'name': None, 'documentation': None, 'target_task_spec': 'ParallelGatewayWorkflow.EndJoin', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'event_definition': {'internal': False, 'external': False, 'typename': 'NoneEventDefinition'}, 'typename': 'EndEvent', 'extensions': {}}, 'Activity_115woll': {'id': 'ParallelGatewayWorkflow_10', 'name': 'Activity_115woll', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_017jnp6'], 'outputs': ['Gateway_0chrwmq'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 140.0}, 'outgoing_sequence_flows': {'Gateway_0chrwmq': {'id': 'Flow_1iiolp4', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_1iiolp4': {'id': 'Flow_1iiolp4', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'var1=6', 'typename': 'ScriptTask', 'extensions': {}}, 'Activity_1g1cdox': {'id': 'ParallelGatewayWorkflow_11', 'name': 'Activity_1g1cdox', 'description': None, 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': ['Gateway_017jnp6'], 'outputs': ['Gateway_0chrwmq'], 'lane': None, 'documentation': None, 'loopTask': False, 'position': {'x': 300.0, 'y': 250.0}, 'outgoing_sequence_flows': {'Gateway_0chrwmq': {'id': 'Flow_110tzrd', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'outgoing_sequence_flows_by_id': {'Flow_110tzrd': {'id': 'Flow_110tzrd', 'name': None, 'documentation': None, 'target_task_spec': 'Gateway_0chrwmq', 'typename': 'SequenceFlow'}}, 'data_input_associations': [], 'data_output_associations': [], 'prescript': None, 'postscript': None, 'script': 'var1=7', 'typename': 'ScriptTask', 'extensions': {}}, 'Root': {'id': 'ParallelGatewayWorkflow_12', 'name': 'Root', 'description': '', 'manual': False, 'internal': False, 'lookahead': 2, 'inputs': [], 'outputs': [], 'typename': 'Simple'}}, 'data_inputs': [], 'data_outputs': [], 'data_objects': {}, 'correlation_keys': {}, 'typename': 'BpmnProcessSpec'}}, 'subprocesses': {}, 'bpmn_messages': []}