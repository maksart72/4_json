import json
import sys
import os


def load_json_file(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except (OSError, json.JSONDecodeError):
        return

def pretty_print_json(json_content):
    pretty_json = json.dumps(json_content, ensure_ascii=False, indent=4)
    print(pretty_json)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python pprint_json.py <path to file>')
        sys.exit(1)
    else:
        filename =  sys.argv[1]
    rawjson = load_json_file(filename)
    if not rawjson:
        print('Can not load JSON file')
        sys.exit(1)
    else:
        pretty_print_json(rawjson)
