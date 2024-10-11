def afd_impar_0s_1s(string):
    count_0 = string.count('0')
    count_1 = string.count('1')
    return count_0 % 2 != 0 and count_1 % 2 != 0
