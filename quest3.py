def afd_exatamente_dois_uns(string):
    estado = 'q0'
    for simbolo in string:
        if estado == 'q0':
            if simbolo == '1':
                estado = 'q1'
        elif estado == 'q1':
            if simbolo == '1':
                estado = 'q2'
        elif estado == 'q2':
            if simbolo == '1':
                estado = 'q3'  
    return estado == 'q2'


print(afd_exatamente_dois_uns("101"))  
print(afd_exatamente_dois_uns("111"))  
