import utils


def componentes(components):
    do__it: bool = True

    while do__it:
        print()
        print('      Menu componentes'.upper())
        print()
        line = '@'
        for n in range(35):
            print(line, end="")

        # Aquí mostraré todas las opciones que tiene el usuario para usar
        print()
        print('@  1. Alta Componente            @')
        print('@  2. Modificar componente       @')
        print('@  0. Volver al menu principal   @')

        for n in range(35):
            print(line, end="")

        print()
        print()
        # Aquí se introduce el número para seleccionar una de las funciones del apartado de Componentes
        # Tiene dos formas de añadir el número, de forma numerica o escrita.
        # Por lo que puedes seleccionarlo como 1 o como uno.
        print('Selecciona un numero del 1 al 3: ')
        number = input()
        if number == '1' or number.upper() == 'UNO':
            alta__Componentes(components)
        elif number == '2' or number.upper() == 'DOS':
            elegir__componente(components)
        elif number == '0' or number.upper() == 'CERO':
            do__it = False
        else:
            print('por favor, introduzca una de las opciones.')
    return components


def alta__Componentes(components):
    """"""
    numero = len(components) + 1
    identificador: str
    tipo_componente: str
    peso: int
    coste: float
    cantidad: int
    bandera = True

    """"""
    print()
    print()
    print('Por Favor, introduzca los siguientes datos.')
    while bandera:
        identifier = input(' - Identificador del componente: ')
        if identifier.isalnum():
            bandera = False
            identificador = identifier
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        typ = input(' - Tipo del componente (Fuente/PB/TG/CPU/RAM/Disco): ').upper()
        if typ == 'FUENTE' or typ == 'PB' or typ == 'TG' or typ == 'CPU' or typ == 'DISCO' or typ == 'RAM':
            bandera = False
            tipo_componente = typ
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        pes = input(' - Peso: ')
        if pes.isnumeric():
            bandera = False
            peso = pes
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        precio = input(' - Precio: ')
        if utils.dato_is_float(precio):
            bandera = False
            coste = precio
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        cant = input(' - Cantidad: ')
        if cant.isnumeric():
            bandera = False
            cantidad = cant
        else:
            print('Por favor, asegúrese de escribirlo bien.')

    components[numero] = [identificador, tipo_componente, peso, coste, cantidad]
    print('Componente guardado')
    return components


def elegir__componente(components):
    bandera = True
    edit__component = []
    while bandera:
        print("Seleccione una como quiere seleccionar el componente a editar:")
        print("1. Identificador")
        print("2. Lista")
        print("0. Volver Atrás")
        print()
        option = input()
        if option == '1':
            edit__component = []
            print()
            while bandera:
                num = input("Introduzca el numero del componente a modificar (o 0 para salir): ")
                if utils.dato_is_int(num) and len(components) >= int(num) > 0:
                    num_int = int(num)
                    bandera = True
                    for k in components[num_int]:
                        edit__component.append(k)
                    while bandera:
                        print("Opciones:")
                        print("1. Editar cantidad")
                        print("2. Editar información")
                        print("3. Eliminar componente")
                        print("0. Dejar como estaba")
                        print()
                        option = input("Seleccione una: ")
                        if option == '1':
                            components[num_int] = edit__quantity(edit__component)
                            bandera = False
                            print('Componente Editado')
                        elif option == '2':
                            components[num_int] = edit__information(edit__component)
                            bandera = False
                            print('Componente Editado')
                        elif option == '3':
                            components.pop(num_int)
                            bandera = False
                        elif option == '0':
                            bandera = False
                        else:
                            print("Por favor, introduzca una de las 2 opciones.")
                elif num == '0':
                    bandera = False
                else:
                    print('Por favor, asegúrese de que ha añadido el numero correcto. ')
                    print()
        elif option == '2':
            while bandera:
                print("Seleccione el componente que quieras modificar: ")
                for key in components:
                    edit__component = []
                    for k in components[key]:
                        edit__component.append(k)
                    parse__string = str(key)
                    print(parse__string + ". " + edit__component[0] + " - " + edit__component[1] + " - " +
                          edit__component[2] +
                          " - " + edit__component[3] + " - " + edit__component[4])

                edit__component = []
                print()
                num = input("Introduzca el numero del componente a modificar (o 0 para salir): ")
                if utils.dato_is_int(num) and len(components) >= int(num) > 0:
                    num_int = int(num)
                    for k in components[num_int]:
                        edit__component.append(k)
                    while bandera:
                        print("Opciones:")
                        print("1. Editar cantidad")
                        print("2. Editar información")
                        print("3. Eliminar componente")
                        print("0. Dejar como estaba")
                        print()
                        option = input("Seleccione una: ")
                        if option == '1':
                            components[num_int] = edit__quantity(edit__component)
                            bandera = False
                            print('Componente Editado')
                        elif option == '2':
                            components[num_int] = edit__information(edit__component)
                            bandera = False
                            print('Componente Editado')
                        elif option == '3':
                            components.pop(num_int)
                            print('Componente eliminado')
                            bandera = False
                        elif option == '0':
                            bandera = False
                        else:
                            print("Por favor, introduzca una de las 2 opciones.")
                elif num == '0':
                    bandera = False
                else:
                    print('Por favor, asegúrese de que ha añadido el numero correcto. ')
                    print()
        elif option == '0':
            bandera = False
        else:
            print("Por favor, introduzca una de las 2 opciones.")
    return components


def edit__information(lista):
    print()
    lista__editada = []
    bandera = True
    for s in lista:
        lista__editada.append(s)
    print('Puedes cambiar los datos a partir de ahora. Los datos que no quieras cambiar puedes dejarlo en blanco.')
    print()
    while bandera:
        identifier = input(' - Identificador del componente[' + lista__editada[0] + ']: ')
        if identifier != '' and identifier.isalnum():
            bandera = False
            lista__editada[0] = identifier
        elif identifier == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        typ = input(' - Tipo del componente (Fuente/PB/TG/CPU/RAM/Disco) [' + lista__editada[1] + ']: ').upper()
        if typ != '' and (typ == 'FUENTE' or typ == 'PB' or typ == 'TG' or typ == 'CPU' or
                          typ == 'DISCO' or typ == 'RAM'):
            bandera = False
            lista__editada[1] = typ
        elif typ == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        pes = input(' - Peso [' + lista__editada[2] + ']: ')
        if pes != '' and pes.isnumeric():
            bandera = False
            lista__editada[2] = pes
        elif pes == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        precio = input(' - Precio [' + lista__editada[3] + ']: ')
        if utils.dato_is_float(precio) and precio != '':
            bandera = False
            lista__editada[3] = precio
        elif precio == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    bandera = True
    while bandera:
        cant = input(' - Cantidad [' + lista__editada[4] + ']: ')
        if cant.isnumeric() and cant != '':
            bandera = False
            lista__editada[4] = cant
        elif cant == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    return lista__editada


def edit__quantity(lista):
    print()
    lista__editada = []
    bandera = True
    for s in lista:
        lista__editada.append(s)
    print('Puedes cambiar la cantidad a partir de ahora. Si no quieres modificar la cantidad,'
          ' puedes dejarlo en blanco.')
    print()
    while bandera:
        cant = input(' - Cantidad [' + lista__editada[4] + ']: ')
        if cant.isnumeric() and cant != '':
            bandera = False
            lista__editada[4] = cant
        elif cant == '':
            bandera = False
        else:
            print('Por favor, asegúrese de escribirlo bien.')
    return lista__editada
