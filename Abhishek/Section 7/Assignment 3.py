def discount(x):
    return x-5

newlist = [10,20,30,40]

result = list(map(discount , newlist))
print(result)
