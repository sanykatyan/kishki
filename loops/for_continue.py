for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

for c in "abc":
    if c == "b":
        continue
    print(c)

for i in range(3):
    continue
    print("never")

for x in [1,2,3]:
    if x == 1:
        continue
    print(x)

for i in range(2):
    continue
