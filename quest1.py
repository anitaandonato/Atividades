def afd_termina_com_1(string):
    estado = 'q0'
    for simbolo in string:
        if estado == 'q0':
            if simbolo == '0':
                estado = 'q0'
            elif simbolo == '1':
                estado = 'q1'
        elif estado == 'q1':
            if simbolo == '0':
                estado = 'q0'
            elif simbolo == '1':
                estado = 'q1'
    return estado == 'q1'

# Teste
print(afd_termina_com_1("101"))  # True
print(afd_termina_com_1("100"))  # False

