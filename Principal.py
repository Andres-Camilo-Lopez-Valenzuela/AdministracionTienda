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
            print('Funcionando de momento')
        case  _:
            print('Tambien esta funcionando')
