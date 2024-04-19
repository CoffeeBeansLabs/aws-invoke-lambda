import os
import pathlib

from inputs import json_to_byte, ensure_json_input
from common.aws_clients import get_client


def run(aws_parameters, input_lambda_name):
    # lambda_client = get_client(service_name='lambda',
    #                            region_name=os.getenv('AWS_REGION'),
    #                            aws_access_key=os.getenv('AWS_ACCESS_KEY'),
    #                            aws_secret_key=os.getenv('AWS_SECRET_KEY'),
    #                            )
    json_byte = json_to_byte(aws_parameters)
    print(json_byte)
    # lambda_client.invoke(FunctionName=input_lambda_name,
    #                      Payload=json_byte)


if __name__ == '__main__':
    input_params = os.getenv('INPUT_PARAMS')
    lambda_name = os.getenv('INPUT_LAMBDA_NAME')
    parsed_value_json = ensure_json_input(input_params)
    run(input_params, lambda_name)
