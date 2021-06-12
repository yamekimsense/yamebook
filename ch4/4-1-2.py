a = "yame"

print (a)
print ( type(a) )

aa = a.encode('ascii') #<class 'str'>

print (aa)
print ( type(aa) )

aaa= a.encode('ascii') #<class 'bytes'>

print (aaa)
print ( type(aaa) ) #<class 'bytes'>


b = b"kim"

print (b)
print ( type(b) ) #<class 'bytes'>


bb = b.decode('ascii')

print (bb)
print ( type(bb) ) #<class 'str'>
