from rich import print  as rprint
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.live import Live
import time


console = Console()



menu_contenido = """

[#45f808]  1.📚 Añadir clase [/]


[#f89208]  2.📝 Corregir examen [/]


[#f8f408]  3.🎓 Ver utlimos examenes [/]


[magenta]  4.🚪 Salir [/]

[bold red]     
Elige una opcion:  
[/bold red]    
                            
"""
system("cls")
menu_principal = Panel(
    Align.center(menu_contenido),
    border_style="#b2ff33",
    title="[blink][#fff933]Corrector examenes[/]"
)



console.print(menu_principal)

def pre_opcion():
    try:
        opcion = int(input())
    except:
        console.print(Panel("[red]❌Introduce un numero por favor[/]",
                                                    title="Error",
                                                    border_style="red",
                                                    width=30))
    return opcion
                                                
                                                

opcion = pre_opcion()




