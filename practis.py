"""x = int(input("enter the num"))
for i in range(1,x+1):
    c=str(i)
    if c[0::]==c[::-1]:
        print(int(c))
"""
"""
s=0
for i in range(152,1001):
    t=i
    while i>0:
        c=i%10
        s=s+c**3
        t=i//10
    if s==t:
        print(i)
 """    

"""    
lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
"""

c=0
s = input("enter string")
m = input("enter char")
for i in range(len(s)):
    if s[i]==m:
        print(f"found at {i} position")
        c+=1
print("total count is",c)

"""
s = input("Enter string")
m = input("Enter string")
l1=s.split()
l2=m.split()
for i in range(len(s)):
    if l1[i]==l2:
        print(l1[i])
"""
