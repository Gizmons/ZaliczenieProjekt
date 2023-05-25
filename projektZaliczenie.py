import yaml
import sys
import json
import xml.etree.ElementTree as ET


def convert_xml_to_json(xml_path, json_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = {root.tag: parse_element(root)}
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


