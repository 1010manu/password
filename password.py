from random import *
l='abcdefghijklmnopqrstuvwxyz'
u=l.upper()
#print(u)
n='0123456789'
s='!@#$%^&*'
string=l+u+n+s
length=32
password=''.join(sample(string,length))
print(password)
