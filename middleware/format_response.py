import json


def format_response_middleware(response):
    data = response.get_json()
    data = format_response(response,data)
    response.data = json.dumps(data).encode("utf-8")
    response.content_type = "application/json"
    return response

def format_response(response, data):
    new_dict = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "_id":
                new_dict["Id"] = str(value["$oid"])
            elif isinstance(value, dict):
                format_response(response, value)
            else:
                camel_case_key = ''.join(x.capitalize() or '_' for x in key.split('_'))
                new_dict[camel_case_key] = value

    return new_dict
