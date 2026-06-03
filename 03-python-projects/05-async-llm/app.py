import asyncio

from rich.console import Console
from rich.prompt import Prompt

from clients.groq_clients import ask_groq
from clients.gemini_clients import ask_gemini
from clients.openrouter_clients import ask_openrouter
from utils.display import display_results


console = Console()


async def main():

    console.print()

    console.print(
        "[bold cyan]Multi-LLM Comparison Tool[/bold cyan]",
        justify="center"
    )

    console.print(
        "[dim]Compare responses across multiple LLMs[/dim]",
        justify="center"
    )

    console.print()

    prompt = Prompt.ask(
        "[bold green]Enter your prompt[/bold green]"
    ).strip()

    console.print()

    if not prompt:
        prompt = "Hello AI"

    with console.status(
        "[bold cyan]Generating responses...[/bold cyan]"
    ):

        results = await asyncio.gather(
            ask_groq(prompt),
            ask_gemini(prompt),
            ask_openrouter(prompt),
            return_exceptions=True
        )

    display_results(results)


if __name__ == "__main__":
    asyncio.run(main())