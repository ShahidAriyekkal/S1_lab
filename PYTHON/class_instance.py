class human:
    def __init__(self,n,p,o):
        self.name=n
        self.place=p
        self.occupation=o
    
    def details(self):
        print(self.name,"\n",self.place,self.occupation)
a,b,c=input("Enter the Name,Place,Occupation : ").split()
instance=human(a,b,c)
instance.details()
