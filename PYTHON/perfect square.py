import math
p=[]
count=0
for i in range(1000,9999,2):
    a=math.sqrt(i)
    if a%1==0:
        for j in str(i):
            if int(j)%2==0:
                count+=1
        if count==4:
            p.append(i)
        count=0
print("The values :" ,p)
