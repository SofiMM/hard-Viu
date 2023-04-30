# Funciones para ayudar al correcto funcionamiento

def dato_is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def dato_is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
