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

menu_principal = Panel(
    Align.center(menu_contenido),
    border_style="#b2ff33",
    title="[blink][#fff933]Corrector examenes[/]",
    expand= True
    
)


                                                
                                                

def main():
    clase = dict()
    # Borramos la pantalla
    system("cls")
    # Mostramos el menu principal
    console.print(menu_principal)
    

    while True:
        system("cls")
        console.print(menu_principal)
        try:
            opcion = int(input())
        except:
            console.print(Panel("[red]❌Introduce un numero por favor[/]",
                                                        title="Error",
                                                        border_style="red",
                                                        width=30))
        # Opcion para añadir clase
        if opcion == 1:
            nombre_clase = prompt("Cual es el nombre de la clase")
            clase[nombre_clase] = nombre_clase
            num_alumnos = int(prompt("Nº de alumnos en clase"))
            for _ in range(num_alumnos):
                
        # Opcion para corrergir examen
        elif opcion == 2:
            pass
        # Opcion para ver los ultimos examenes corregidos
        elif opcion == 3:
            pass
        elif opcion == 4:
            input("Muchas gracias por usar el programa")
            break
        else:
            console.print(Panel("[red]❌Introduce un opcion valida por favor[/]",
                                                    title="Error",
                                                    border_style="red",
                                                    width=50,
                                                    
                                                    ))

            input()
  
    


if __name__ == "__main__":
    main()