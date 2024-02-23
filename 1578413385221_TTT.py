s='-------|---------|-------'
a=[['A','|','B','|','C'],s,['D','|', 'E','|','F'],s,['G','|','H','|','I']]
for t in a:
   print(t)
z=0
while True:
   y=input('Player 1,Enter BOX')
   for p in range(0,len(a)):
      for q in range(0,len(a)):
         if y==a[p][q]:
            a[p][q]='0'
            for n in a:
               print(n)
               z+=1
   x=input('Player 2,Enter BOX')
   for i in range(0,len(a)):
      for j in range(0,len(a)):
         if x==a[i][j]:
            a[i][j]='X'
            for k in a:
               print(k)
               z+=1
               if z<10:
                  break
print('Hello World')
               

    
