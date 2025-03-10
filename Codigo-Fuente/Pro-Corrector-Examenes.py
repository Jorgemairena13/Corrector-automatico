from rich import print  
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.table import Table


import time

console = Console()

menu_contenido = """

[#45f808]  1.📚 Añadir clase [/]


[#f89208]  2.📝 Corregir examen [/]


[#3155fa]  3.🎓 Ver utlimos examenes [/]


[#f8f408]  4. ⚡Correcion rapida [/]

[magenta]  5.🚪 Salir [/]

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
style = Style.from_dict({
    'prompt': '#ffd02f',  
    '': '#33b5ff',
})
                                       
def main():
    clase = dict()
    opcion = 0
    # Bucle principal
    while True:
        system("cls") # Borramos la pantalla
        #Mostamos el menu principal
        console.print(menu_principal)
        
        try: # Le pedimos la opcion
            opcion = int(prompt('',style=style))
        except: # Si no introduce un numero le mostramos mensaje de error
            console.input(Panel("[red]❌ Introduce una opcion valida por favor[/]",
                                                        title="Error",
                                                        border_style="red",
                                                        width=40))
      
        # Opcion para añadir clase
        if opcion == 1:
            contador = 1 # Comenzamos el contador

            #Preguntamos por el nombre de la clase
            nombre_clase = prompt("Cual es el nombre de la clase: ",style=style)
            # Comprobamos que la clase no esta ya guardada
            if nombre_clase in clase:
                console.input(Panel("[red]❌ La clase ya esta añadida[/]",
                                                        title="Error",
                                                        border_style="red",
                                                        width=40))
                continue
            elif nombre_clase == '':
                console.input(Panel("[red]❌ No se se admiten espacios vacios[/]",
                                                        title="Error",
                                                        border_style="red",
                                                        width=40))
                continue

            # En el diccionario creado anteriormente guardamos el nombre de la clase con una clave alumnos y una lista donde estaran los alumnos
            clase[nombre_clase] = {"alumnos": []}
            
            # Pedimos el numero de alumnos
            try:
                num_alumnos = int(prompt("Nº de alumnos en clase: ",style=style))
            except:
                console.input(Panel("[red]❌Introduce un numero por favor[/]",
                                                        title="Error",
                                                        border_style="red",
                                                        width=40))
                del(clase[nombre_clase])
                continue

            for _ in range(num_alumnos):
                # Preguntamos el nombre de los alumnos que haya en la clase
                nombre_alumno = prompt('Nombre del alumno a añadir: ',style=style).capitalize()

                # Lo introducimos en la lista que hemos creado como un diccionario con su id y su nombre
                clase[nombre_clase]["alumnos"].append({'id':contador,'Nombre': nombre_alumno})

                # Sumamos 1 al contador para que no haya repeticiones
                contador += 1

            # Mostramos mesaje de confirmacion
            console.print(Panel("[green]✅ Clase añadida correctamente[/]",
                                                    
                                                    border_style="green",
                                                    width=50,
                                                    
                                                    ))
            prompt()
               
               
        # Opcion para corrergir examen
        elif opcion == 2:

            # Contador 
            contador = 1

            # Preguntamos el numero de preguntas
            while True:
                try: # Preguntamos por el numero de preguntas
                    num_preguntas = int(prompt('Cuantas preguntas tiene el examen?\n',style=style))
                    if num_preguntas == 0:
                        console.input(Panel("[red]❌ El examen no puede tener 0 preguntas[/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=40))
                        system('cls')
                        continue

                    
                    break
                except: # Si nos da error le mostramos ese mensaje y le volvemos a preguntar
                    console.input(Panel("[red]❌Introduce un numero por favor[/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=40))
                    system('cls')
                    continue
        

            # Hacemos los calculos de las preguntas buenas y malas
            pregunta_correcta = 10 / num_preguntas
            pregunta_incorrecta =  round(pregunta_correcta / 3,2)

            # Creamos la lista donde vamos a guardar las respuestas correctas
            lis_pregu_corre = []
            lista_opciones = ['A','B','C','D']

            # Hacemos el bucle para preguntar por las correctas
            for _ in range(num_preguntas):
                system('cls')

                while True:
                    # Pedimos la respuesta correcta
                    pregunta_corregida = prompt(f'Escribe la solucion de la pregunta {contador} [A/B/C/D]',style=style).upper()
                    if pregunta_corregida in lista_opciones:
                        # Añadimos a la lista de preguntaas corregidas
                        lis_pregu_corre.append(pregunta_corregida)
                        break
                    else:
                        console.input(Panel("[red]❌La opcion solo puede ser [A/B/C/D] [/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=40))
                        system('cls')
                        continue

                contador += 1 # Aumentamos en 1

            # Mostramos las clases para corregir el examen   
            for a,nombre in enumerate(clase.keys(),start=1):
                console.print(f'[#0316ff]{a}-{nombre}[/]')

            # Pedimos el nombre de la clase que se va a corregir el examen
            while True:
                try:
                    nombre_clase = prompt('Nombre clase: ',style=style)
                    if nombre_clase in clase:
                        system("cls")
                        break
                except:
                    console.print(Panel("[red]❌La clase no existe[/]",
                                                                title="Error",
                                                                border_style="red",
                                                                width=40))
                    continue
            
            # Recorremos los nombres de los alumnos
            for alumno in clase[nombre_clase]['alumnos']:
                
                # Variables para el numero de buenas y malas
                contador = 0
                preguntas_buenas = 0
                preguntas_malas = 0
                sin_contestar = 0
                nota_final = 0

                # Le mostramos el alumno que se le va a corregir el examen
                console.print(f'Examen a corregir de {alumno["Nombre"]}\n')

                # Recorremos la lista de preguntas correctas
                for _ in lis_pregu_corre :
                    # Bucle para validar la respuesta 
                    while True:
                        # Le pedimos la respuesta del alumno
                        respuesta = prompt(f'Escribe la respuesta a la pregunta {contador + 1}\nIntro para respuesta sin contestar',style=style).upper()
                        # Espacio para mejor vision
                        print('')
                        

                        # Si esta en la lista de opciones o es intro
                        if respuesta in lista_opciones or respuesta == '':
                            break
                        else: # Le mostramos el mensaje de error
                            console.input(Panel(f"[red]❌Introduce una opcion valida por favor [{lista_opciones}][/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=60))
                            system('cls')
                            continue
                        
                    # Comparamos la respuesta si es intro es sin contestar
                    if respuesta == '':
                        # Le sumamos uno a las sin contestar
                        sin_contestar += 1
                        
                    # Comparamos que la respuesta sea igual que la de la lista que vamos rbuscando con el contador
                    elif respuesta == lis_pregu_corre[contador]:
                        preguntas_buenas += 1# Le sumamos 1 a las buenas
                        
                    # Si no es ninguna de las opciones la damos por mala
                    else:
                        preguntas_malas += 1 # Le sumamos 1  a las malas
                    contador += 1
                
                #Hacemos los calculos de las buenas con lo que vale cada preguta buena
                final_pregu_buenas = preguntas_buenas * pregunta_correcta

                #Hacemos los calculos de las malas con lo que vale cada preguta mala
                final_pregu_malas = preguntas_malas * pregunta_incorrecta

                # Calculamos la nota final restando las malas a las buenas
                nota_final = final_pregu_buenas - final_pregu_malas

                # La redondeamos para no tener tantos decimales
                nota_final = round(nota_final,2)

                system('cls')
                # Mostramos cuantas pregutas a tenido bien mal y sin contestar
                console.print(f'[#f7ff03]El alumno {alumno["Nombre"]} a tenido[/]\n[#3cff03]Preguntas buenas: {preguntas_buenas}[/]\n[#ff0303]Preguntas malas: {preguntas_malas}[/]\n[#0316ff]Preguntas sin contestar: {sin_contestar}[/]\n')
                if nota_final >= 5:
                    console.print(f'La nota final es de [#27ff58]{nota_final}[/]')
                else:
                    console.print(f'La nota final es de [#fc0000]{nota_final}[/]')

                # Guardamos la nota final en  el alumno y una clave nota  


                alumno["nota"] = nota_final
                prompt()
                system('cls')
            
            
        # Opcion para ver los ultimos examenes corregidos
        elif opcion == 3:
            for a,nombre in enumerate(clase.keys(),start=1):
                console.print(f'[#0316ff]{a}-{nombre}[/]')
            nombre_clase = prompt('De que clase quieres mostrar el ultimo examen?\n')
            while True:
                tabla = Table(
                            title="[blink]📋 Lista de alumnos[/]",
                            header_style="bold bright_cyan",
                            border_style="bright_yellow",
                        )
                tabla.add_column('Nombre')
                tabla.add_column('Nota')
                try:
                    for alumno in clase[nombre_clase]['alumnos']:
                         tabla.add_row(
                             str(alumno['Nombre']),
                             #Hacemos la condicion para que salga de color verde si es mas de 5 o rojo si es menos 
                             f"[#fc0000]❌ {alumno['nota']}[/]" if alumno['nota'] <= 5 else f"[#27ff58]✅ {alumno['nota']}[/]")
                          
                        #print(f'{alumno['Nombre']} {alumno['nota']}')
                    console.print(tabla)
                    prompt('Pulsa enter para continuar',style=style)

                    break
                except:
                    console.print(Panel("[red]❌No hay notas para esta clase[/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=60))
                    prompt('Pulsa enter para continuar',style=style)
                    system('cls')
                    break
            

        elif opcion == 4:
            while True:
                try: # Preguntamos por el numero de preguntas
                    num_preguntas = int(prompt('Cuantas preguntas tiene el examen?\n',style=style))
                    if num_preguntas == 0:
                        console.input(Panel("[red]❌ El examen no puede tener 0 preguntas[/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=40))
                        system('cls')
                        continue

                    
                    break
                except: # Si nos da error le mostramos ese mensaje y le volvemos a preguntar
                    console.input(Panel("[red]❌Introduce un numero por favor[/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=40))
                    system('cls')
                    continue

            pregunta_correcta = 10 / num_preguntas
            pregunta_incorrecta =  round(pregunta_correcta / 3,2)

            contador = 0
            preguntas_buenas = 0
            preguntas_malas = 0
            sin_contestar = 0
            nota_final = 0

            lis_pregu_corre = []
            lista_opciones = ['A','B','C','D']

            for _ in range(num_preguntas):
                system('cls')

                while True:
                    # Pedimos la respuesta correcta
                    pregunta_corregida = prompt(f'Escribe la solucion de la pregunta {contador + 1} [A/B/C/D]',style=style).upper()
                    contador += 1
                    if pregunta_corregida in lista_opciones:
                        # Añadimos a la lista de preguntaas corregidas
                        lis_pregu_corre.append(pregunta_corregida)
                        break
                    else:
                        console.input(Panel("[red]❌La opcion solo puede ser [A/B/C/D] [/]",
                                                            title="Error",
                                                            border_style="red",
                                                            width=40))
                        system('cls')
                        continue
            contador = 0 
            for _ in lis_pregu_corre :
            
                # Bucle para validar la respuesta 
                while True:
                    # Le pedimos la respuesta del alumno
                    respuesta = prompt(f'Escribe la respuesta a la pregunta {contador + 1}\nIntro para respuesta sin contestar',style=style).upper().strip()
                    
                    # Espacio para mejor vision
                    print('')

                    # Si esta en la lista de opciones o es intro
                    if respuesta in lista_opciones or respuesta == '':
                        break
                    else: # Le mostramos el mensaje de error
                        console.input(Panel(f"[red]❌Introduce una opcion valida por favor [{lista_opciones}][/]",
                                                        title="Error",
                                                        border_style="red",
                                                        width=60))
                        system('cls')
                        continue
                
                

                # Comparamos la respuesta si es intro es sin contestar
                if respuesta == '':
                    # Le sumamos uno a las sin contestar
                    sin_contestar += 1
                    
                # Comparamos que la respuesta sea igual que la de la lista que vamos rbuscando con el contador
                elif respuesta == lis_pregu_corre[contador]:
                    preguntas_buenas += 1# Le sumamos 1 a las buenas
                    
                # Si no es ninguna de las opciones la damos por mala
                else:
                    preguntas_malas += 1 # Le sumamos 1  a las malas
                contador += 1
            
            #Hacemos los calculos de las buenas con lo que vale cada preguta buena
            final_pregu_buenas = preguntas_buenas * pregunta_correcta

            #Hacemos los calculos de las malas con lo que vale cada preguta mala
            final_pregu_malas = preguntas_malas * pregunta_incorrecta

            # Calculamos la nota final restando las malas a las buenas
            nota_final = final_pregu_buenas - final_pregu_malas

            # La redondeamos para no tener tantos decimales
            nota_final = round(nota_final,2)

            system('cls')
            # Mostramos cuantas pregutas a tenido bien mal y sin contestar
            console.print(f'[#f7ff03]El alumno a tenido[/]\n[#3cff03]Preguntas buenas: {preguntas_buenas}[/]\n[#ff0303]Preguntas malas: {preguntas_malas}[/]\n[#0316ff]Preguntas sin contestar: {sin_contestar}[/]\n')
            if nota_final > 5:
                console.print(f'La nota final es de [#27ff58]{nota_final}[/]')
            else:
                console.print(f'La nota final es de [#fc0000]{nota_final}[/]')
            prompt()
        elif opcion == 5:
            prompt("Muchas gracias por usar el programa",style=style)
            break
        


if __name__ == "__main__":
    main()