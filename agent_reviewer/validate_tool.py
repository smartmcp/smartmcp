from openapi_spec_validator import validate


def validate_tool(swagger_dict: dict) -> str:
    """Validate the swagger dictionary"""
    try:
        validate(swagger_dict)
        return "Valid"
    except Exception as e:
        return f"Invalid: {str(e)}"
