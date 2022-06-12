n = int(input())
d = {}
memory = ""
for i in range(n):
    aux = input()
    if aux in d:
        d.update({aux: d.get(aux) + 1})
        if 3 in d.values():
            memory = aux
            break
    else:
        d.update({aux: 1})

if memory:
    print(memory)
else:
    print("JOC OK")