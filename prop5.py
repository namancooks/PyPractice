c = 0
n = int(input("enter num"))
for i in range(2,n):
    if n%i==0:
        c+=1
        break
if c>0:
    print("composite")
else:
    print("prime")
    
    
        
      