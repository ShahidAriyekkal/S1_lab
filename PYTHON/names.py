names=[]
for i in range(5):
    a=input("Enter the name ")
    names.append(a)
list2=[]
for i in names[:]:
    if(i.startswith('a') or i.startswith('A')):
        list2.append(i)
        print(i,"added")
        names.remove(i)
        print(i,"removed")
else:
    print("after names removed ",names)
    print("names with a",list2)
