f = open("temp.txt", 'r')

lines = f.readlines()

print (type(lines))

print (lines[0])

print (lines)

for line in lines:
    print(line)

f.close()