import json
import sys
import os


def load_json_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)

def pretty_print_json(json_content):
    pretty_json = json.dumps(json_content, ensure_ascii=False, indent=4)
    print(pretty_json)

if __name__ == '__main__':
    FILE = sys.argv[1]
    RAWJSON = load_json_file(FILE)
    pretty_print_json(RAWJSON)
