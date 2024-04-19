import json


def ensure_json_input(input_params: str):
    try:
        return json.loads(input_params)
    except ValueError as e:
        print('Not valid JSON')
        return None


def json_to_byte(input_json):
    json_string = json.dumps(input_json)
    json_bytes = json_string.encode('utf-8')
    return json_bytes
