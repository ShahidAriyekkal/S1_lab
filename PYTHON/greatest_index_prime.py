x=[2,3,17]
print("the greatest : " ,max(x))
c=max(x)
f='prime'
print("position: ",(x.index(c)+1))
for i in range (2,c):
    if(c%i==0):
        f='Not prime'
        break
print(f)
