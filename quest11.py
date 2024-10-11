def afd_impar_as(string):
    estado = 'q0'
    for simbolo in string:
        if simbolo == 'a':
            estado = 'q1' if estado == 'q0' else 'q0'
    return estado == 'q1'
