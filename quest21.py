def afn_a_apos_b(string):
    return all(string[i] == 'a' for i in range(len(string)) if 'b' in string[:i])
