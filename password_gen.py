from os import system
import random
system('CLS')

ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lcase = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
sym = '~!@#$%^&*'

ans = ucase + lcase + num + sym
len = 12

for i in range (1,11):
    password = "".join(random.sample(ans,len))
    print("Genrated Password : ",password)