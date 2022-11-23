
class Emitter:

    @classmethod
    def emit(cls, serialized, serializer_version, output_filename):
        with open(output_filename, "w") as f:
            f.write(f"""
from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter


SERIALIZER_VERSION = "{serializer_version}"
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
