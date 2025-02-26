from blessed import Terminal

term = Terminal()

opciones = ['Opción 1', 'Opción 2', 'Opción 3']
selected = 0

with term.cbreak():
    with term.hidden_cursor():
        while True:
            print(term.clear())
            
            for i, opcion in enumerate(opciones):
                if i == selected:
                    print(term.move(i+1, 1) + term.reverse + opcion + term.normal)
                else:
                    print(term.move(i+1, 1) + opcion)
            
            key = term.inkey()
            
            if key.code == term.KEY_UP and selected > 0:
                selected -= 1
            elif key.code == term.KEY_DOWN and selected < len(opciones)-1:
                selected += 1
            elif key == 'q':
                break