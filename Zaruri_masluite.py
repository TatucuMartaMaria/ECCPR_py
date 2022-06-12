N = int(input())
l = []
for i in range(N):
    l.append(int(input()))
d = {}
for el in l:
    d.update({el: l.count(el)})
if (max(d.values()) - min(d.values())) <= (N / 10):
    print(0)
else:
    print(1)
