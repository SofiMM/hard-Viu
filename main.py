"""
Nombre: Sofia Montagud Mengual

En este proyecto voy a elaborar el programa propuesto como actividad para la asignatura de Metología de Programación.

"""

from submenus import componentes, distribuidores, equipos, despechar, dias, info__sistemas, ficheros

# Diccionarios que se utilizaran en la aplicación.
components = {}
equips = {}
distribuidor = {}


# Esta función va a mostrarnos por pantalla un menú donde nos da las opciones principales del programa.
def print_menu():
    # Primero voy a crear una variable booleana para que haya un bucle while infinito que solo se para cuando el
    # usuario decida salirse del programa.
    global components
    global distribuidor
    global equips
    do__it: bool = True
    while do__it:
        print()
        print('      Menu principal'.upper())
        print()
        line = '·'
        for n in range(30):
            print(line, end="")

        # Aquí mostraré todas las opciones que tiene el usuario para usar
        print()
        print('·  1. Componentes            ·')
        print('·  2. Equipos                ·')
        print('·  3. Distribuidores         ·')
        print('·  4. Despechar              ·')
        print('·  5. Dias                   ·')
        print('·  6. Info sistema           ·')
        print('·  7. Ficheros               ·')
        print('·  0. Salir                  ·')

        for n in range(30):
            print(line, end="")

        print()
        print()
        # Aquí se introduce el número para seleccionar una de las funciones de los sub apartados de la aplicación.
        # Tiene dos formas de añadir el número, de forma numerica o escrita.
        # Por lo que puedes seleccionarlo como 1 o como uno.
        print('Selecciona un numero del 0 al 7: ')
        number = input()
        if number == '1' or number.upper() == 'UNO':
            components = componentes.componentes(components)
        elif number == '2' or number.upper() == 'DOS':
            equipos.equipos(equips)
        elif number == '3' or number.upper() == 'TRES':
            distribuidor = distribuidores.distribuidores(distribuidor)
        elif number == '4' or number.upper() == 'CUATRO':
            despechar.despechar()
        elif number == '5' or number.upper() == 'CINCO':
            dias.dias()
        elif number == '6' or number.upper() == 'SEIS':
            info__sistemas.info__Sistema()
        elif number == '7' or number.upper() == 'SIETE':
            ficheros.fichero()
        elif number == '0' or number.upper() == 'CERO':
            print('Gracias por usar esta aplicación.')
            do__it = False
        else:
            print('por favor, introduzca una de las opciones.')


if __name__ == '__main__':
    print_menu()
