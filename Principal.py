# Este es el archivo Principal
import modulos.ui as ui
import modulos.opcionclientes as opc
import modulos.opcionesempleados as ope
from clear import clear

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
            clear()
            ui.men2()
            opc.opcionclientes()
        case 2:
            clear()
            ui.men3()
            ope.opcionempleados()
        case _:
            print('Opcion no valida 🤐')
            
