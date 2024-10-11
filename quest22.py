def afd_diferenca_mult3(string):
    diff = abs(string.count('a') - string.count('b'))
    return diff % 3 == 0
