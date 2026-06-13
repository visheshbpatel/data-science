from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown


console = Console()


def display_results(results):

    console.rule("[bold blue]LLM Response Comparison[/bold blue]")

    for result in results:

        provider = result["provider"]
        model = result["model"]

        if "response" in result:
            content = result["response"]

        else:
            content = str(result["error"])

        panel = Panel(
            Markdown(content),
            title=f"{provider} | {model}",
            border_style="cyan",
            expand=False
        )

        console.print(panel)
        console.print()