import asyncio
from typing import Any
from agents import Agent, Runner, AgentHooks, AgentHookContext


class AgentHandler(AgentHooks):
    def __init__(self, name: str):
        super().__init__()
        print(f"Initializing AgentHandler for agent: {name}")

    async def on_start(self, ctxt: AgentHookContext, agent: Agent) -> None:
        print(f"Agent {agent.name} started")

    async def on_end(self, ctxt: AgentHookContext, agent: Agent, output: Any) -> None:
        print(f"Agent {agent.name} ended with output: {output}")


async def main():
    a = Agent(
    name="Test AgentHooks",
    instructions="You are knowledgeable on anything.",
    hooks=AgentHandler("Test AgentHooks")
    )

    result = await Runner.run(a, "Write a poem about recursion in programming.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

