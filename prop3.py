n = int(input("Enter num1 "))
m = int(input("Enter num2 "))
p = int(input("Enter num3 "))
"""
if n>m:
    if n>p:
        print("n is greatest")
    else:
        print("p is greatest")
else:
    print("m is greatest")

if n<m:
    if n<p:
        print("n is smallest")
    else:
        print("p is smallest")
else:
    print("m is smallest")
        
"""

l = n
s = n
if m>l:
    l=m
if p>l:
    l=p
if m<s:
    s=m
if p<s:
    s=p
print("largest is",l)
print("smallest is",s)

