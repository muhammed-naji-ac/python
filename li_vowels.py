li=["a","e","i","o","u"]
w=input("enter some words").lower()
fv=[]
for char in w:
    if char in li:
        fv.append(char)

print(fv)