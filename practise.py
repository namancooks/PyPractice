def power_num(n,p):
    if p==0:
        return 1
    else:
        return n**p
"""    
n = eval(input("Enter num"))
p = eval(input("Enter num"))
print(power_num(n,p))
"""
def list_py(i,m):
    if n==1:
        return False
    else:
        l[i]=l[m] and l[m]=l[i]
        return l

l = []
n = int(input("Enter last index value"))
for i in range(n):
    m = int(input("enter num"))
    l.append(m)
print(list_py(2,3))