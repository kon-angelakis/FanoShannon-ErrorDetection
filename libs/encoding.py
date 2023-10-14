#-----Cyclic Code Check implementation and entropy calculator-----

import math

def calc_entropy(binarystring):
    count0 = binarystring.count('0')
    count1 = binarystring.count('1')
    prob0 = count0 / len(binarystring)
    prob1 = count1 / len(binarystring)

    #Returns H(x) entropy result of the given binary string
    return(-((prob0*math.log2(prob0)) + (prob1*math.log2(prob1))))



#this is the crc code (same as in Server)
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        #go through every bit, if bits same then result 0 otherwise result 1
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


# Does Modulo-2 Division Necessary for crc encoding
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    checkword = tmp
    return checkword


def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder

    return codeword