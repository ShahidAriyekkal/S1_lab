a=int(input("Enter the number you want "))
b=1
temp=a
for i in range(1,a+temp):
    if i<=a:
        print(i*"*")
    else:
        print((temp-b)*"*")
        b+=1
