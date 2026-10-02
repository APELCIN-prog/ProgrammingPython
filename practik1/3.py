from random import *
import string
simvols = '!@#$%^&*'
stroca = string.ascii_uppercase
s = []
for i in range(3):
    s.append(str(randint(1, 9)))
    s.append(choice(stroca))
for i in range(2):
    s.append(choice(simvols))
shuffle(s)
print(''.join(s))
