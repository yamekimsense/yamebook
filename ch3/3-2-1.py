#Lotto Number Generator
#Use Python3

import random

lotto = []
duplicate=0

while 1>0:

   number = random.randrange(1,46)
   print ("number = ", number)

   for i in lotto:
       print ("   for loop ", i)
       if number == i:
           duplicate=1
           print ("--- duplicated ")

   if duplicate==0:
       lotto.append(number)
       print ("   lotoo number is ", lotto, "\n")

   if duplicate==1:
       print ("***************************")
       print ("duplicated is ", number)
       print ("lotto is", lotto, "\n")

   if len(lotto)  == 6:
       break

   duplicate = 0

print ("==================")
print ("lotto numbers are ", lotto)


'''
variables

lotto : list type lotto number
number : lotto number each time 
duplicate : if duplicated 1, if not 0
'''