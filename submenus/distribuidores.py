import utils


def distribuidores(distribuidor):
    do__it: bool = True
    while do__it:
        print()
        print('      Menu distribuidores'.upper())
        print()
        line = '@'
        for n in range(40):
            print(line, end="")

        # Aquí mostraré todas las opciones que tiene el usuario para usar
        print()
        print('@  1. Alta Distribuidor                @')
        print('@  2. Modificar Distribuidor           @')
        print('@  0. Volver al menu principal         @')

        for n in range(40):
            print(line, end="")

        print()
        print()
        # Aquí se introduce el número para seleccionar una de las funciones del apartado de Distribuidores
        # Tiene dos formas de añadir el número, de forma numerica o escrita.
        # Por lo que puedes seleccionarlo como 1 o como uno.
        print('Selecciona un numero del 1 al 3: ')
        number = input()
        if number == '1' or number.upper() == 'UNO':
            alta__Distribuidores(distribuidor)
        elif number == '2' or number.upper() == 'DOS':
            elegir__distribuidor(distribuidor)
        elif number == '0' or number.upper() == 'CERO':
            do__it = False
            return distribuidor
        else:
            print('por favor, introduzca una de las opciones.')
    return distribuidor


def alta__Distribuidores(distribuidor):
    """"""
    numero = len(distribuidor) + 1
    nombre: str
    dias_entrega: int
    direction: str
    bandera = True
    """"""
    print()
    print()
    print('Por Favor, introduzca los siguientes datos.')
    while bandera:
        identifier = input(' - Nombre del distribuidor: ')
        if identifier.isalnum():
            bandera = False
            nombre = identifier
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        days = input(' - Tiempo de entrega desde fábrica en días: ')
        if days.isnumeric():
            bandera = False
            dias_entrega = int(days)
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        direc = input(' - Dirección: ')
        if len(direc) < 100:
            bandera = False
            direction = direc
        else:
            print('Por favor, asegúrese de escribirlo bien.')

    distribuidor[numero] = [nombre, dias_entrega, direction]
    print('distribuidor guardado')
    return distribuidor


def elegir__distribuidor(distribuidor):
    bandera = True
    edit__distribuidor = []
    while bandera:
        print("Seleccione una como quiere seleccionar el distribuidor a editar:")
        print("1. Identificador")
        print("2. Lista")
        print("0. Volver Atrás")
        print()
        option = input()
        if option == '1':
            edit__distribuidor = []
            print()
            num = input("Introduzca el numero del distribuidor a modificar: ")
            if utils.dato_is_int(num) and len(distribuidor) >= int(num) > 0:
                num_int = int(num)
                bandera = True
                for k in distribuidor[num_int]:
                    edit__distribuidor.append(k)
                while bandera:
                    print("Opciones:")
                    print("1. Editar información")
                    print("2. Dar de baja al distribuidor")
                    print("0. Dejar como estaba")
                    print()
                    option = input("Seleccione una: ")
                    if option == '1':
                        distribuidor[num_int] = edit__information(edit__distribuidor)
                        bandera = False
                        print('Distribuidor Editado')
                    elif option == '3':
                        distribuidor.pop(num_int)
                        bandera = False
                    elif option == '0':
                        bandera = False
                    else:
                        print("Por favor, introduzca una de las 3 opciones.")
            elif num == '0':
                bandera = False
        elif option == '2':
            while bandera:
                print("Seleccione el distribuidor que quieras modificar: ")
                for key in distribuidor:
                    edit__distribuidor = []
                    for k in distribuidor[key]:
                        edit__distribuidor.append(k)
                    parse__string = str(key)
                    print(parse__string + ". " + edit__distribuidor[0] + " - " +str(edit__distribuidor[1])  + " - " +
                          edit__distribuidor[2])
                    edit__distribuidor = []
                    print()
                    num = input("Introduzca el numero del distribuidor a modificar (o 0 para salir): ")
                    if utils.dato_is_int(num) and len(distribuidor) >= int(num) > 0:
                        num_int = int(num)
                        for k in distribuidor[num_int]:
                            edit__distribuidor.append(k)
                        while bandera:
                            print("Opciones:")
                            print("1. Editar información")
                            print("2. Eliminar distribuidor")
                            print("0. Dejar como estaba")
                            print()
                            option = input("Seleccione una: ")
                            if option == '1':
                                distribuidor[num_int] = edit__information(edit__distribuidor)
                                bandera = False
                                print('Distribuidor Editado')
                            elif option == '2':
                                distribuidor.pop(num_int)
                                print('Distribuidor eliminado')
                                bandera = False
                            elif option == '0':
                                bandera = False
                            else:
                                print("Por favor, introduzca una de las 3 opciones.")
                    elif num == '0':
                        bandera = False
                    else:
                        print('Por favor, asegúrese de que ha añadido el numero correcto. ')
                        print()
        elif option == '0':
            bandera = False
        else:
            print("Por favor, introduzca una de las 2 opciones.")
    return distribuidor


def edit__information(lista):
    print()
    lista__editada = []
    bandera = True
    for s in lista:
        lista__editada.append(s)
    print('Puedes cambiar los datos a partir de ahora. Los datos que no quieras cambiar puedes dejarlo en blanco.')
    print()
    while bandera:
        identifier = input(' - Nombre del distribuidor[' + lista__editada[0] + ']: ')
        if identifier != '' and identifier.isalnum():
            bandera = False
            lista__editada[0] = identifier
        elif identifier == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        days = input(' - Tiempo de entrega desde fábrica en días[' + lista__editada[1] + ']: ')
        if days.isnumeric():
            bandera = False
            lista__editada[1] = int(days)
        elif days == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        direc = input(' - Dirección: ')
        if len(direc) < 100:
            bandera = False
            lista__editada[1] = direc
        elif bandera == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    return lista__editada
