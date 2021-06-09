file = open("demo.txt", 'w')
content = file.write("my name is abhishek")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("demo.txt", 'a')
content = file.write("my name is medishetty")
file.close()
