
f = open ("temp.txt", 'w')

for i in range (1,6):
    x  = str (i)+"\n"
    f.write (x)

f.close()
