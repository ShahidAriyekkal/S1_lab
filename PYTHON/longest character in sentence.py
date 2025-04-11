word=input("Enter a sentence : ").split()
temp=len(word[0])
w=word[0]
for i in word:
    if temp<len(i):
        temp=len(i)
        w=i
print("The Longest word :",w,"has :",temp," characters")