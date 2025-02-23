# Este es el archivo Principal
import modulos.ui as ui

# Muestra el menú
ui.men1()

opcion = None

try:
    opcion = int(input('Por favor elija una opción: '))
except ValueError:
    print('Ingrese un número para continuar porfavor 😓')

if opcion is not None:
    match opcion:
        case 1:
            ui.men2()
        case 2:
            ui.men3()
        case _:
            print('Opcion no valida 🤐')
            
