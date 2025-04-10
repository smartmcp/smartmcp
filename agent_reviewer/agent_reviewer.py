class AgentReviewer:
    """Agent that reviews the swagger file and returns a list of issues OR calls the agent to generate code"""

    @staticmethod
    def validate_swagger_from_string(swagger_string: str) -> list[str] | None:
        """Validate the swagger file and return a list of issues"""
