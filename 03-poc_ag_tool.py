import asyncio
from agents import Agent, Runner, function_tool


##


@function_tool
def find_doubitchou():
    """
    this tool finds doubitchou
    """
    return "- Oui, effectivement on a un petit peu l'impression que c'est fait à la main, quoi... \
            -Oui, oui, oui, c'est fait à la main, c'est roulé à la main sous les aisselles"


@function_tool
def find_kloug():
    """
    this tool find kloug
    """
    return "- Mais... mais qu'est ce que c'est que cette matière ? Mais c'est d'la merde ? - Non, c'est kloug."


async def main():

    a = Agent(
    name="Tools",
    instructions="You are knowledgeable on anything.",
    tools=[find_doubitchou, find_kloug]
    )

    result = await Runner.run(a, "Do you know where are doubitchou and kloug?")
    print(result.final_output)


##


if __name__ == "__main__":
    asyncio.run(main())

