# read the file and store all the lines to the list


with open("demo.txt", 'r') as reader:
    line = reader.readlines()
    reversed(line)
    with open("demo.txt", 'w') as writer:
        for line in reversed(line):
            writer.write(line)



