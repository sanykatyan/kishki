nums = [1, 2, 3, 4]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)



nums = [-2, 3, -1, 5]
res = list(filter(lambda x: x > 0, nums))
print(res)



words = ["hi", "", "ok"]
res = list(filter(lambda w: w != "", words))
print(res)
