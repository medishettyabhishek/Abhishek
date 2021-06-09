file = open("demo.txt", 'w')
content = file.write("helloworld")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("demo.txt", 'a')
content = file.write("helloworld2")
file.close()

