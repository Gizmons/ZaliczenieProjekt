
def convert_json_to_yaml(json_path, yaml_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
    with open(yaml_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file)


