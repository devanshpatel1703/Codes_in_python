l=[]
l2=[]
for i in range(1,6,1):
    a=input("Enter element :")
    l.append(a)
for x in l:
    if x not in l2:
        l2.append(x)
print(l2)
