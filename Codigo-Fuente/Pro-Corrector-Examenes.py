from rich import print  as print
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
            contador = 1
            nombre_clase = prompt("Cual es el nombre de la clase")
            
            clase[nombre_clase] = {"alumnos": []}
            
            num_alumnos = int(prompt("Nº de alumnos en clase"))
            for _ in range(num_alumnos):
                nombre_alumno = prompt('Nombre del alumno a añadir: ')
                clase[nombre_clase]["alumnos"].append({'id':contador,'Nombre': nombre_alumno})
                contador += 1

            console.print(Panel("[green]✅ Clase añadida correctamente[/]",
                                                    
                                                    border_style="green",
                                                    width=50,
                                                    
                                                    ))
               
            input()       
            


        # Opcion para corrergir examen
        elif opcion == 2:

            # Contador 
            contador = 1

            # Preguntamos el numero de preguntas
            num_preguntas = int(prompt('Cuantas preguntas tiene el examen?'))
            # Hacemos los calculos de las preguntas buenas y malas

            pregunta_correcta = 10 / num_preguntas
            pregunta_incorrecta =  round(pregunta_correcta / 3,2)

            # Creamos la lista donde vamos a guardar las respuestas correctas
            lis_pregu_corre = []

            # Hacemos el bucle para preguntar por las correctas
            for _ in range(num_preguntas):
                # Pedimos la respuesta correcta
                pregunta_corregida = input(f'Escribe la solucion de la pregunta {contador} [A/B/C/D]').upper()
                # Añadimos a la lista de preguntaas corregidas
                lis_pregu_corre.append(pregunta_corregida)
                contador += 1 # Aumentamos en 1

            # Mostramos las clases para corregir el examen   
            console.print(clase)
            
            preguntas_buenas = 0
            preguntas_malas = 0
            sin_contestar = 0
            nombre_clase = input('Nombre clase: ')
            
            for alumno in clase[nombre_clase]['alumnos']:
                contador = 0
                console.print(f'Examen a corregir de {alumno}')
                for _ in lis_pregu_corre :
                    respuesta = prompt(f'Escribe la respuesta a la pregunta {contador + 1}').upper()
                    
                    if respuesta == '':
                        sin_contestar += 1
                        
                    elif respuesta == lis_pregu_corre[contador]:
                        preguntas_buenas += 1
                        
                    else:
                        preguntas_malas += 1
                        
                    
                    final_pregu_buenas = preguntas_buenas * pregunta_correcta
                    final_pregu_malas = preguntas_malas * pregunta_incorrecta
                    nota_final = final_pregu_buenas - final_pregu_malas
                    nota_final = round(nota_final,2)
                    print(nota_final)
                    contador += 1
                    input()
                alumno["nota"] = nota_final
                print(clase[nombre_clase]["alumnos"])

                    
                

            # Bucle para añadir la nota del alumno
            for alumno in clase[nombre_clase]['alumnos']:
                nota = float(input(f'Nota para {alumno["Nombre"]}: '))
                alumno["nota"] = nota  # Añadir la nota directamente al diccionario del alumno
                
            print(clase[nombre_clase]["alumnos"])
            


            
            input()

            
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