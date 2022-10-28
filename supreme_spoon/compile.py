from backend.python_csp import PythonCSPBackend
from frontend.bpmn import BpmnFrontend
from util import by_id

class Compiler:

    @classmethod
    def _extract_sequence_flows(self, data):
        sequence_flows = filter(lambda d: d[0] == "sequenceFlow", data)
        non_sequence_flows = filter(lambda d: d[0] != "sequenceFlow", data)

        return (sequence_flows, non_sequence_flows)

    @classmethod
    def _resolve(self, sequence_flows):
        sequence_flows_by_id = by_id(sequence_flows)

        map_to = lambda r: lambda v: (v[0], v[1], sequence_flows_by_id[v[2]][1][r])
        resolvers = {"incoming": map_to("sourceRef"), "outgoing": map_to("targetRef")}

        def resolve_elem_value(v):
            return resolvers[v[0]](v) if v[0] in resolvers else v

        def resolver(elem):
            return (elem[0], elem[1], list(map(resolve_elem_value, elem[2])))

        return resolver

    @classmethod
    def _resolve_sequence_flows(self, process_data):
        sequence_flows, elems = self._extract_sequence_flows(process_data[2])
        resolved_elems = map(self._resolve(sequence_flows), elems)
        return (process_data[0], process_data[1], list(resolved_elems))

    @classmethod
    def compile(self, input_filename, output_filename):
        process_data = BpmnFrontend.parse(input_filename)
        flowed_process_data = list(map(self._resolve_sequence_flows, process_data))
        code = PythonCSPBackend.codegen(flowed_process_data)

        with open(output_filename, 'w') as f:
            f.write(code)

if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    Compiler.compile(input_filename, output_filename)
