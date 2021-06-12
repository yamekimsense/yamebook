
f = open ("temp.txt", 'a')

for i in range (6,11):
    x  = str (i)+"\n"
    f.write (x)

f.close()
