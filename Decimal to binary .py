n=int(input("Enter the number"))
m=n
list1=[]
while n>0:
    r=n%2
    list1.append(r)
    n=n//2
list1.reverse()
print('Binary of the number',m,'is',list1)


############################################################