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
