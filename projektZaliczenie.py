

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

