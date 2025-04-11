from dishka import Provider, provide, Scope
from openai import OpenAI


class RootProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_llm(self) -> OpenAI:
        return OpenAI(model="gpt-4o-mini")
