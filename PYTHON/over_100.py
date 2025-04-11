l1=[]
l2=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    x=int(input("Enter the value"))
    l1.append(x)
    if x>100:
        l2.append('over')
    else:
        l2.append(x)
print(l1)
print(l2)
