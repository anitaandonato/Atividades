def afd_mesmo_inicio_fim(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1]

# Teste
print(afd_mesmo_inicio_fim("101"))  # True
print(afd_mesmo_inicio_fim("100"))  # False
