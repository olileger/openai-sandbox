import asyncio
from agents import Agent, Runner, function_tool


##


@function_tool
def get_weather(city: str) -> str:
    """
    this tool gets weather
    """
    print(f"Getting weather for {city}...")
    return "The weather is sunny with a high of 25 degrees Celsius."

@function_tool
def swap_text(text: str) -> str:
    """
    this tool swap a given text
    """
    print(f"Swapping text: {text}...")
    return text[::-1]


async def main():

    a = Agent(
    name="Test Agent",
    instructions="You are knowledgeable on anything. Rely on the tools to answer the user's question.",
    tools=[get_weather, swap_text]
    )

    result = await Runner.run(a, "Quel temps fait-il à Paris ?!")
    print(result.final_output)

    result = await Runner.run(a, "Swap this: 'Hello World ?!'")
    print(result.final_output)

##


if __name__ == "__main__":
    asyncio.run(main())

