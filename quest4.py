def afd_um_zero(string):
    estado = 'q0'
    for simbolo in string:
        if estado == 'q0':
            if simbolo == '0':
                estado = 'q1'
    return estado == 'q1'


print(afd_um_zero("101"))  
print(afd_um_zero("111"))  
