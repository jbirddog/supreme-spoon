from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.spiff.serializer.task_spec_converters import ManualTaskConverter
from SpiffWorkflow.spiff.serializer.task_spec_converters import ScriptTaskConverter

from emit import Emitter

class Dependencies:

    SPEC_CONVERTERS = {
        "ManualTask": (ManualTaskConverter, "ManualTaskConverter"),
        "Script Task": (ScriptTaskConverter, "ScriptTaskConverter"),
    }

    @classmethod
    def compile_time_spec_converters(cls):
        def sc_cls(tup):
            return tup[0]

        return list(map(sc_cls, cls.SPEC_CONVERTERS.values()))
    
    @classmethod
    def runtime_spec_converters(cls, tasks):
        deps = set()
        for task in tasks:
            spec_type = task.task_spec.spec_type
            if spec_type in cls.SPEC_CONVERTERS:
                deps.add(cls.SPEC_CONVERTERS[spec_type][1])
        return sorted(list(deps))


class Compiler:
    SERIALIZER_VERSION = "1.0-supreme-spoon"

    @classmethod
    def parse_workflow(cls, process, bpmn_files):
        parser = SpiffBpmnParser()
        parser.add_bpmn_files(bpmn_files)
        top_level = parser.get_spec(process)
        subprocesses = parser.find_all_specs()
        return BpmnWorkflow(top_level, subprocesses)

    @classmethod
    def get_serializer(cls):
        wf_spec_converter = BpmnWorkflowSerializer.configure_workflow_spec_converter(
            Dependencies.compile_time_spec_converters()
        )
        return BpmnWorkflowSerializer(wf_spec_converter, version=cls.SERIALIZER_VERSION)

    @classmethod
    def compile(cls, process, input_filename, output_filename):
        wf = cls.parse_workflow(process, [input_filename])
        tasks = wf.get_tasks()
        serialized = cls.get_serializer().workflow_to_dict(wf)
        spec_converters = Dependencies.runtime_spec_converters(tasks)

        Emitter.emit(process, serialized, cls.SERIALIZER_VERSION, spec_converters, output_filename)

if __name__ == "__main__":
    import sys

    # TODO: argparse
    #process = sys.argv[1]
    #input_filename = sys.argv[2]
    #output_filename = sys.argv[3]

    process = "CopyBPMNFiles"
    input_filename = "examples/copybpmn/copybpmn.bpmn"
    output_filename = "examples/copybpmn/copybpmn.py"

    Compiler.compile(process, input_filename, output_filename)
