import sys
hour = input()
n = int(input())
memory = []
difference2 = sys.maxsize
for i in range(n):
    aux = input().split(" ")
    aux[0] = int(aux[0].replace(":", ""))
    difference = aux[0] - int(hour.replace(":", ""))
    if (difference > 0):
        if difference2 == sys.maxsize:
            memory.append([aux[0], aux[1], aux[2]])
            difference2 = difference
        elif (difference < difference2):
            memory.pop()
            memory.append([aux[0], aux[1], aux[2]])
            difference2 = difference
        elif (difference == difference2):
            if(int(memory[0][1]) > int(aux[1])):
                memory.pop()
                memory.append([aux[0], aux[1], aux[2]])

print(memory[0][2])