
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
    def emit(self, data):
        print(list(data))

class Compiler:
    @classmethod
    def compile(self, input_filename, output_filename):
        process_data = BpmnFrontend.parse(input_filename)
        PythonBackend.emit(process_data)

if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    Compiler.compile(input_filename, output_filename)

    print(f"ok: {input_filename} -> {output_filename}")
