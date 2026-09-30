from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from app import ask


console = Console()


while True:
    
    q = Prompt.ask("[bold cyan]Tú[/bold cyan]")
    
    if q.lower() in ["exit", "quit", "salir"]:
        break
    
    response = ask(q)
    
    
    console.print(
        Panel(
            response, 
            title="AI",
            border_style="green"
        )
    )
    
    