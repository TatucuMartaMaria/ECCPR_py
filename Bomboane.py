n = int(input())
s = []
def intElementsList(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l
s[:] = intElementsList(input("\n").split(" "))
l = []
for i in range(n):
    l.append(intElementsList(input().split(" ")))

money = 0
happy = 0
flavor_candy = []

for i in range(n):
    money = money + s[i]
    if money >= l[i][0]:
        money = money - l[i][0]
        happy = happy + l[i][1]
        flavor_candy.append(l[i][1])
    else:
        if flavor_candy == []:
            happy = happy - l[i][1]
        elif l[i][1] >= max(flavor_candy):
            happy = happy - l[i][1]

print(happy)