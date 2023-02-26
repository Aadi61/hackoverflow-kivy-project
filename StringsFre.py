a=input("Enter a string")
b=input("Enter the character to count")
count=0
for ch in a:
    if ch==b:
        count+=1
print(b+" repeats "+ str(count) +" number of times" )
