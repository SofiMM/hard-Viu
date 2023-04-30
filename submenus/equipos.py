

def equipos(equips):
    do__it: bool = True
    while do__it:
        print()
        print('      Menu equipos'.upper())
        print()
        line = '@'
        for n in range(35):
            print(line, end="")

        # Aquí mostraré todas las opciones que tiene el usuario para usar
        print()
        print('@  1. Alta Equipo                @')
        print('@  2. Modificar Equipo           @')
        print('@  0. Volver al menu principal   @')

        for n in range(35):
            print(line, end="")

        print()
        print()
        # Aquí se introduce el número para seleccionar una de las funciones del apartado de Equipos
        # Tiene dos formas de añadir el número, de forma numerica o escrita.
        # Por lo que puedes seleccionarlo como 1 o como uno.
        print('Selecciona un numero del 1 al 3: ')
        number = input()
        if number == '1' or number.upper() == 'UNO':
            alta__Equipos()
        elif number == '2' or number.upper() == 'DOS':
            equipos()
        elif number == '0' or number.upper() == 'CERO':
            do__it = False
        else:
            print('por favor, introduzca una de las opciones.')


def alta__Equipos(equips):
    """"""
    numero = len(equips) + 1
    identificador: str
    """"""
    print()
    print()
    print('Por Favor, introduzca los siguientes datos.')
    while bandera:
        identifier = input(' - Identificador del equip: ')
        if identifier.count() >= 3:
            bandera = False
            identificador = identifier
        else:
            print('Por favor, asegúrese de escribirlo bien.')

    equips[numero] = {identificador}
