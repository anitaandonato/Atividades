def valida_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido!"
    
    cpf_mascarado = 'XXX' + cpf[3:9] + 'XX'
    return cpf_mascarado


print(valida_cpf("70468293493")) 
print(valida_cpf("12345678901"))  
print(valida_cpf("00000000000"))  
print(valida_cpf("01234567890"))  
print(valida_cpf("12345678abc")) 
print(valida_cpf("123456789"))   
