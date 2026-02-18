from agents import Agent, Runner
from pydantic import BaseModel

wr = Agent(name="Writer",
           handoff_description="Specialist agent for writing poem.",
           instructions="You write poem based on the given topic. 10 lines maximum.")

re = Agent(name="Reviewer",
           handoff_description="Specialist agent for reviewing poem.",
           instructions="You review the poem and give feedback. format: bulletpoints.")

orchestrator = Agent(name="Orchestrator",
                     instructions="You determine which agent to use based on the user's question",
                     handoffs=[wr, re])

result = Runner.run_sync(orchestrator, "Write a poem about recursion in programming.")
print(result.final_output)