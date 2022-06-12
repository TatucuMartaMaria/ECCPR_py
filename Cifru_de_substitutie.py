text = input("\n")
chars = input("\n").split(" ")
L = []
d = {}
for el in chars:
    L += [el.split(",")]
d = dict(L)
output = ""
for el in text:
    if el in d.keys():
        output += d[el]
    else:
        output += el
print(output)