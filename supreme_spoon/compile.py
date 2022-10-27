
# frontend/bpmn.py
from lxml import etree

class BpmnFrontend:
    @classmethod
    def _parse_xml(self, bpmn_filename):
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

    # move to middle
    @classmethod
    def _build_process_maps(self, process_data):
        elems, flows = {}, {}

        for value in process_data[2]:
            d = elems if value[0] != "sequenceFlow" else flows
            d[value[1]["id"]] = value

        return (process_data[0], elems, flows)

    @classmethod
    def parse(self, bpmn_filename):
        data = self._parse_xml(bpmn_filename)
        data = map(self._build_process_maps, data)
        print(list(data))

# backend/python.py
class PythonBackend:
    def emit(self):
        pass

class Compiler:
    def compile(self):
        pass

if __name__ == "__main__":
    import sys

    bpmn_filename = sys.argv[1]
    python_filename = sys.argv[2]

    BpmnFrontend.parse(bpmn_filename)

    print(f"ok: {bpmn_filename} -> {python_filename}")
