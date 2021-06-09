import re

pattern = r"eggs"

if re.findall(pattern,"baconeggseggseggsbacon"):
    print("match found")

else:
    print("match not found")

print(re.findall(pattern,"baconeggseggseggsbacon"))


