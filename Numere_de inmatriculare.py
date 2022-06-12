string1 = ['AB', 'AR', 'AG', 'B', 'BC', 'BH', 'BN', 'BT', 'BV', 'BR', 'BZ', 'CS', 'CL', 'CJ', 'CT', 'CV', 'DB', 'DJ',
           'GL', 'GR', 'GJ', 'HR', 'HD', 'IL', 'IS', 'IF', 'MM', 'MH', 'MS', 'NT', 'OT', 'PH', 'SM', 'SJ', 'SB', 'SV',
           'TR', 'TM', 'TL', 'VS', 'VL', 'VN']

s = []
aux = ''
l = []
while True:
    try:
        aux = input()
        if aux == '':
            break
        l = aux.split(" ")
        if (l[0] in string1) and (len(l[1]) > 1 and len(l[1]) < 4 and l[1].isnumeric()) and \
                (len(l[2]) == 3 and l[2].isupper() and l[2].isalpha()):
            s.append(aux)
    except EOFError:
        print('a')
        break

for i in range(len(s)):
    print(s[i])