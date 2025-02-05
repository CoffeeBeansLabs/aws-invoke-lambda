import json


def ensure_json_input(input_params: str):
    try:
        return json.loads(input_params)
    except ValueError as e:
        print('Not valid JSON')
        return None


def env_to_param(env_line: str):
    env_line = env_line.strip()
    env_line = env_line.split(sep="=", maxsplit=1)
    return dict(name=env_line[0], value=env_line[1])


def ensure_env_input(input_params: str):
    param_lines = input_params.strip().split(sep="\n")
    return [param_line.strip() for param_line in param_lines]


def value_to_aws_parameter(param_name, param_value):
    parsed_value_json = ensure_json_input(param_value)
    if parsed_value_json is None:
        return dict(name=param_name, value=param_value)
    value = parsed_value_json.get('value') if parsed_value_json.get('value') is not None else None
    return dict(name=param_name, value=value)


def parse_input_params(input_params: str):
    parsed_params_json = ensure_json_input(input_params)
    if parsed_params_json is not None:
        return {key: value_to_aws_parameter(key, value) for key, value in parsed_params_json.items()}
    parsed_params_env = ensure_env_input(input_params)
    parsed_aws_params_env = [env_to_param(env_param) for env_param in parsed_params_env]
    return {p["name"]: p for p in parsed_aws_params_env}

