newlist = [13, 14, 15, 17, 1, 2, 2, 3 ,5]

result = list(filter(lambda x: x %2 == 0, newlist))
print(result)