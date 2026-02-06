i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)

n = 0
while n < 3:
    n += 1
    if n == 1:
        continue
    print(n)

x = 0
while x < 4:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

i = 0
while i < 2:
    i += 1
    continue
    print("never")

i = 0
while i < 1:
    i += 1
    continue
