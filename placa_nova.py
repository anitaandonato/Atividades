def valida_placa(placa, texto):
    paises = ['Argentina', 'Brasil', 'Venezuela', 'Paraguai', 'Uruguai']
    
    if len(placa) == 7 and placa[:3].isalpha() and placa[3].isdigit() and placa[4].isalpha() and placa[5:].isdigit():
        if any(pais in texto for pais in paises):
            return "Mercosul"
        else:
            return "Modelo Antigo"
    else:
        return "Placa está com caracteres fora do padrão!"

print(valida_placa("ABC1D23", "São Paulo - SP"))
print(valida_placa("A2C1D23", "Rio de Janeiro - RJ"))
print(valida_placa("A4C1D23", "Brasil"))
print(valida_placa("ABC1D23", "Belo Horizonte - MG"))
