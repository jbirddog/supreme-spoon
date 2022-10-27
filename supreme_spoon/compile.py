
# frontend/bpmn.py
from lxml import etree

class BpmnFrontend:
    @classmethod
    def parse(self, bpmn_filename):
        with open(bpmn_filename, 'r') as f:
            bpmn = etree.parse(f)

        namespaces = {
            "bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "dc": "http://www.omg.org/spec/DD/20100524/DC",
            "bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
        }

        def find(node, xpath):
            return node.xpath(xpath, namespaces=namespaces)

        def localname(node):
            return etree.QName(node).localname

        def tupled(node):
            value = list(map(tupled, node)) if len(node) > 0 else node.text
            return (localname(node), node.attrib, value)

        process_nodes = find(bpmn, "/bpmn:definitions/bpmn:process")
        process_data = map(tupled, process_nodes)
        return process_data

# backend/python.py
class PythonBackend:
    @classmethod
    def _csp(self, kinda_ast):
        prog = """
def start_event(k):
    print("Hello from start_event")
    k()
"""
        return prog

    @classmethod
    def emit(self, kinda_ast):
        return self._csp(kinda_ast)

class Compiler:

    @classmethod
    def _extract_sequence_flows(self, data):
        def is_sequence_flow(datum):
            return datum[0] == 'sequenceFlow'
        def is_not_sequence_flow(datum):
            return not is_sequence_flow(datum)

        sequence_flows = filter(is_sequence_flow, data)
        non_sequence_flows = filter(is_not_sequence_flow, data)

        return (sequence_flows, non_sequence_flows)

    @classmethod
    def _by_id(self, data):
        return {d[1]["id"]: d for d in data}

    # {'SequenceFlow_0lvudp8': ('sequenceFlow', {'id': 'SequenceFlow_0lvudp8', 'sourceRef': 'StartEvent_1', 'targetRef': 'EndEvent_0q4qzl9'}, None)}
    # [('startEvent', {'id': 'StartEvent_1'}, [('outgoing', {}, 'SequenceFlow_0lvudp8')]), ('endEvent', {'id': 'EndEvent_0q4qzl9'}, [('incoming', {}, 'SequenceFlow_0lvudp8')])]

    @classmethod
    def _resolve(self, sequence_flows):
        sequence_flows_by_id = self._by_id(sequence_flows)

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
        return list(resolved_elems)

    @classmethod
    def compile(self, input_filename, output_filename):
        process_data = BpmnFrontend.parse(input_filename)
        flowed_process_data = map(self._resolve_sequence_flows, process_data)
        prog = PythonBackend.emit(flowed_process_data)

        with open(output_filename, 'w') as f:
            f.write(prog)

if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    Compiler.compile(input_filename, output_filename)

    print(f"ok: {input_filename} -> {output_filename}")
