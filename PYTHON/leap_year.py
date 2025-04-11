x=int(input("Enter to which year you want : "))
for i in range(2024,x):
    if(i%400==0 or (i%4==0 and i%100!=0)):
        print(i," is a leap year")
else:
    print("\n over")
