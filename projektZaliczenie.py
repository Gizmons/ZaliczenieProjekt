
def convert_yaml_to_json(yaml_path, json_path):
    with open(yaml_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


