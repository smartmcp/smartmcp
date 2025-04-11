from typing import Callable
from llama_index.core.tools.function_tool import FunctionTool
from llama_index.core.agent.workflow.function_agent import FunctionAgent
from openai import OpenAI


class AgentReviewerBuilder:
    def __init__(
        self,
        llm: OpenAI,
        parse_tool_fn: Callable[[str], dict],
        validate_tool_fn: Callable[[dict], str],
        evaluate_tool_builder: Callable[[OpenAI], Callable[[str], str]],
    ) -> None:
        self._llm = llm
        self._tools = [
            FunctionTool.from_defaults(fn=parse_tool_fn),
            FunctionTool.from_defaults(fn=validate_tool_fn),
            FunctionTool.from_defaults(fn=evaluate_tool_builder(llm)),
        ]

    def build(self) -> FunctionAgent:
        return FunctionAgent(
            llm=self._llm,
            tools=self._tools,
            system_prompt="You are an agent that can use tools to validate swagger and evaluate it.",
        )
