import json, sys

filepath = sys.argv[1]

def load_data(filepath):
    fo = open(filepath)
    str = fo.read()
    data = json.loads(str)
    return data

def pretty_print_json(content):
    content = json.dumps(content, ensure_ascii = False, indent=4)
    return content

if __name__ == '__main__':
    content = load_data(filepath)
    print(pretty_print_json(content))
