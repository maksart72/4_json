import json, sys

filepath = sys.argv[1]

def load_json_file(filepath):
    fo = open(filepath)
    str = fo.read()
    json_raw = json.loads(str)
    return json_raw

def pretty_print_json(content):
    content = json.dumps(content, ensure_ascii = False, indent=4)
    return content

if __name__ == '__main__':
    content = load_json_file(filepath)
    print(pretty_print_json(content))
