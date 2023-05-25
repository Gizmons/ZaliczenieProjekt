

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
