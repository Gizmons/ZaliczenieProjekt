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


def parse_element(element):
    if len(element) == 0:
        return element.text
    result = {}
    for child in element:
        child_data = parse_element(child)
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result


def convert_json_to_xml(json_path, xml_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
    root_element = ET.Element(list(data.keys())[0])
    build_element(root_element, data[list(data.keys())[0]])
    tree = ET.ElementTree(root_element)
    tree.write(xml_path)


def build_element(parent_element, data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    element = ET.Element(key)
                    build_element(element, item)
                    parent_element.append(element)
            else:
                element = ET.Element(key)
                build_element(element, value)
                parent_element.append(element)
    else:
        parent_element.text = str(data)


def convert_yaml_to_json(yaml_path, json_path):
    with open(yaml_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def convert_json_to_yaml(json_path, yaml_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
    with open(yaml_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file)


def convert_data(file1, file2):
    file1_extension = file1.split('.')[-1]
    file2_extension = file2.split('.')[-1]

    if file1_extension == 'xml' and file2_extension == 'json':
        convert_xml_to_json(file1, file2)
    elif file1_extension == 'json' and file2_extension == 'xml':
        convert_json_to_xml(file1, file2)
    elif file1_extension == 'yaml' and file2_extension == 'json':
        convert_yaml_to_json(file1, file2)
    elif file1_extension == 'json' and file2_extension == 'yaml':
        convert_json_to_yaml(file1, file2)
    else:
        print("Nieobsługiwane formaty plików.")
        print("Obsługiwane formaty: .xml -> .json, .json -> .xml, .yaml -> .json, .json -> .yaml")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Sposób użycia: python program.py pathFile1.x pathFile2.y")
        print("gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml).")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_data(input_file, output_file)

    print("Konwersja danych zakończona pomyślnie.")
