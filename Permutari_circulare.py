n = int(input())

#Transformare nr n in nr binar m
def decimalToBinary(decimal):
    binary = ""
    while decimal != 0:
        binary = str((decimal - (decimal//2)*2)) + binary
        decimal = decimal//2
    return binary

def binaryToDecimal(binary):
    decimal = 0
    for i in range(len(str(binary))):
        decimal += (binary % 10) * (2**i)
        binary = binary // 10
    return decimal

m = decimalToBinary(n)

#Lista cu nr in format binar
l = []
w = 0
aux = m
for i in range(len(str(m))):
    w = str(aux)[-1] + str(aux)[:-1]
    l.append(str(aux)[-1] + str(aux)[:-1])
    aux = w

#Lista cu nr in format decimal
L = []
for i in range(len(l)):
    L.append(binaryToDecimal(int(l[i])))

print(max(L))