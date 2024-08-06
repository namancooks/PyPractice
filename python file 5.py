d={}
s=int(input("Enter dictionary values"))
for i in range(0,s):
    m=input("Enter key")
    n=input("Enter key values")
    d[m]=n
print(d)
l=list(d)
l.sort()
sortdict={j:d[j] for j in l}
print(sortdict)
print("Made by Naman Jain")