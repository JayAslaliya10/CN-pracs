def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]

    while pick < len(dividend):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]

        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]

        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword


def encodeData(data, divisor):

    l_divisor = len(divisor)
    appended_data = data + '0'*(l_divisor-1)
    remainder = mod2div(appended_data, divisor)
    codeword = data + remainder
    print("Remainder : ", remainder)
    print("Encoded Data (Data + Remainder) : ", codeword)


data = input("Enter the data : ")
divisor = input("Enter the divisor : ")
encodeData(data, divisor)