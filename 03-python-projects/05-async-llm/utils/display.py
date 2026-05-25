from rich.console import Console
from rich.table import Table


console = Console()


def display_results(results):

    table = Table(title="LLM Response Comparison")

    table.add_column("Provider", style="cyan", no_wrap=True)
    table.add_column("Response", style="white")

    for result in results:

        provider = result["provider"]

        if "response" in result:
            response = result["response"]

        else:
            response = str(result["error"])

        table.add_row(provider, response)

    console.print(table)