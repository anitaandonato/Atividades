def reconhece_placa(string):
    if len(string) == 7 and string[:3].isalpha() and string[3] == '-' and string[4:].isdigit():
        return string + " placa correta."
    else:
        return string + " placa fora do padrão."

print(reconhece_placa('ABC-123'))
print(reconhece_placa('ABC-1234'))
print(reconhece_placa('XYZ-5678'))
print(reconhece_placa('ABCDE-123'))
print(reconhece_placa('AB-123'))
