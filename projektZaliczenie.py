

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


