from dishka import FromDishka, Provider, provide, Scope
from openai import OpenAI

from agent_reviewer.agent import AgentReviewerBuilder
from parse_tool import parse_tool
from validate_tool import validate_tool
from evaluate_tool import evaluate_tool_builder


class ReviewerProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_agent_reviewer_builder(
        self,
        llm: FromDishka[OpenAI],
    ) -> AgentReviewerBuilder:
        return AgentReviewerBuilder(
            llm=llm,
            parse_tool_fn=parse_tool,
            validate_tool_fn=validate_tool,
            evaluate_tool_builder=evaluate_tool_builder,
        )
