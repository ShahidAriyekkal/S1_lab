list=[2,3,5,6]
list2=[]
list3=[]
for i in list:
    if(i%2==0):
        list2.append(i)
    else:
        list3.append(i)
else:
    print("Even list : ",list2)
    print("Odd list : ",list3)
