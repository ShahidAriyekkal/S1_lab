n=int(input("Enter the number of names: "))
x=[]
c=0
for i in range (n):
    y=input("Enter the name : ")
    x.append(y)
for i in x[:]:
    for j in i.lower():
        if 'a' in j:
            c=c+1
print(c)

