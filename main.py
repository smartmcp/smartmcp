from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow.function_agent import FunctionAgent

from tools import tools

load_dotenv()

llm = OpenAI(model="gpt-4o-mini")

workflow = FunctionAgent(
    llm=llm,
    system_prompt="You are an agent that can use tools to parse swagger into MCP (Model Context Protocol) format.",
    tools=tools,
)
