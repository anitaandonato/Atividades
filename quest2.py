def afd_par_de_zeros(string):
    estado = 'q0'
    for simbolo in string:
        if estado == 'q0':
            if simbolo == '0':
                estado = 'q1'
        elif estado == 'q1':
            if simbolo == '0':
                estado = 'q0'
    return estado == 'q0'

# Teste
print(afd_par_de_zeros("1010"))  # True
print(afd_par_de_zeros("100"))   # False
