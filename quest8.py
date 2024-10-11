def afn_num_zeros_div3(string):
    return string.count('0') % 3 == 0


print(afn_num_zeros_div3("000"))  
print(afn_num_zeros_div3("0100")) 
