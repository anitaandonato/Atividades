def afd_contem_101(string):
    estado = 'q0'
    for simbolo in string:
        if estado == 'q0':
            if simbolo == '1':
                estado = 'q1'
        elif estado == 'q1':
            if simbolo == '0':
                estado = 'q2'
        elif estado == 'q2':
            if simbolo == '1':
                estado = 'q3'
    return estado == 'q3'
