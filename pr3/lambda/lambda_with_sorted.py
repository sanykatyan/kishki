nums = [5, 1, 3]
print(sorted(nums, key=lambda x: -x))



words = ["apple", "hi", "banana"]
print(sorted(words, key=lambda w: len(w)))



pairs = [(1, 3), (2, 1)]
print(sorted(pairs, key=lambda p: p[1]))
