
def convert_json_to_xml(json_path, xml_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
    root_element = ET.Element(list(data.keys())[0])
    build_element(root_element, data[list(data.keys())[0]])
    tree = ET.ElementTree(root_element)
    tree.write(xml_path)

