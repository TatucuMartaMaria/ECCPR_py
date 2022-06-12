n = int(input("\n"))
digits = []
digits[0:n] = input("\n").split(" ")
d = {}
for i in range(n):
    digits[i] = int(digits[i])
copy_digits = sorted(set(digits))
for el in digits:
    d.update({el: digits.count(el)})
s = ""
if n % 2 == 0:
    for el in copy_digits:
        s = s + str(el) * (d[el] // 2)
    s = s[::-1] + s
else:
    memory = ''
    for key, value in d.items():
        if value % 2 == 1:
            memory = key
    for el in copy_digits:
        s = s + str(el) * (d[el] // 2)
    s = s[::-1] + str(memory) + s

if len(s) == n:
    print(int(s))
else:
    print(0)