m, n, p = input("\n").split(" ")
l = []
neintegralisti = []
d = {}
for i in range(2*int(m)):
        aux = []
        if i%2 == 0:
                l += input().split("\n")
        else:
                aux = list(input().split(" "))
                medie = 0
                for j in range(int(n)):
                        if int(aux[j]) >= 5:
                                medie += int(aux[j])
                        else:
                                neintegralisti.append(l[len(l)-1])
                if (medie/int(n)) >= 8:
                        d[l[len(l) - 1]] = medie / int(n)

for el in neintegralisti:
        if el in d.keys():
                d.pop(el)

performanta = {}
for key in d.keys():
        if d[key] == max(d.values()):
                performanta[key] = d[key]

if (len(d)-len(performanta)) > int(p):
        print(p)
else:
        print(len(d)-len(performanta))

for key in performanta.keys():
        print(key + " " + str('{:.2f}'.format(performanta[key])))
