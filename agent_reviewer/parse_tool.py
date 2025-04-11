import json


def parse_tool(swagger_string: str) -> dict:
    """Parse the swagger string into a dictionary"""
    try:
        swagger_dict = json.loads(swagger_string)
        return swagger_dict
    except json.JSONDecodeError:
        return {"error": "Invalid JSON"}
