from typing import Callable
from openai import OpenAI


def evaluate_tool_builder(llm: OpenAI) -> Callable[[str], str]:
    def evaluate_tool(swagger_string: str) -> str:
        """Evaluate the swagger string"""

        prompt = f"""Evaluate the quality of this Swagger documentation. For each API method, check:
1. Does it have a clear description?
2. Are input and output models properly defined?
3. Are response codes documented?
4. If authentication is mentioned in the description, verify that there are methods requiring authentication.

Provide a detailed analysis of the documentation quality:
{swagger_string}"""

        response = llm.complete(prompt=prompt)

        return response.text

    return evaluate_tool
