def _by_id(data):
    return {d[1]["id"]: d for d in data}


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
        def preamble():
            return """
identity = lambda x: x

def end_event(id, k):
    def impl(data):
        print(f"In end_event: {id}")
        return k(data)
    return impl

def start_event(id, k):
    def impl(data):
        print(f"In start_event: {id}")
        return k(data)
    return impl
"""

        def main(process_id, csp):
            return f"""
if __name__ == "__main__":
    print("Running '{process_id}'...")
    workflow = {csp}
    result = workflow({{}})
    print(f"result: {{result}}")
"""
        steps = kinda_ast[0][2]
        start_event = list(filter(lambda n: n[0] == "startEvent", steps))[0]
        steps_by_id = _by_id(steps)

        func_map = {
            "startEvent": "start_event",
            "endEvent": "end_event",
        }

        def outgoing(step):
            return list(filter(lambda n: n[0] == "outgoing", step[2]))

        def form_csp(step):
            f = func_map[step[0]]
            id = step[1]["id"]
            outgoing_steps = list(map(lambda s: steps_by_id[s[2]], outgoing(step)))
            if len(outgoing_steps) == 0:
                k = "identity"
            else:
                assert len(outgoing_steps) == 1, "TODO"
                k = form_csp(outgoing_steps[0])
            csp = f"{f}(\"{id}\", {k})"
            return csp

        csp = form_csp(start_event)
        process_id = kinda_ast[0][1]["id"]
        prog = "\n".join([preamble(), main(process_id, csp)])

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
    def _resolve(self, sequence_flows):
        sequence_flows_by_id = _by_id(sequence_flows)

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
        prog = PythonBackend.emit(flowed_process_data)

        with open(output_filename, 'w') as f:
            f.write(prog)

if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    Compiler.compile(input_filename, output_filename)
