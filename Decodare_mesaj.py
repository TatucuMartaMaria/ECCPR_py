d = {}
d[0] = " "
for i in range(26):       #A = 65 ; Z=91    !ASCII
    d[i+1] = chr(65 + i)
message = input()
l = []
i = 0
output = ""
while i < len(message):
    if int(message[i:(i+2)]) <= 26:
        l.append(message[i:(i+2)])
        i = i+2
    else:
        l.append(message[i:(i+1)])
        i = i + 1
for el in l:
    output = output + d[int(el)]
print(output, "\n")