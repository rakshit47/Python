U=int(input('Enter the amount of electricity consumed'))

if U<=200:
    E=U*2.50
elif U>201 and U<=500:
    E=U*3.80
elif U>501 and U<=1000:
    E=U*4.75
else:
    E=U*7.50

S=E*12.5/100

print('Amount on your Electricity consumed =',E)
print('Service Tax on your consumption =',S)
print('Net amount on your consumption is....',E+S)
print('NOTE : Save Electricity because Bijli ka bill tera baap bharega')
