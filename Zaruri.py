N = int(input())
l = []
for i in range(N):
    aux = input().split(" ")
    for j in range(len(aux)):
        l.append(int(aux[j]))

print(21 * N - sum(l))