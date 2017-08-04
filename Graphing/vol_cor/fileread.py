f = open("data.txt")
line = f.read()
line = str(line)
line = line.split(':')
print line
f.close()

