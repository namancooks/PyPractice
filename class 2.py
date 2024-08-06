c = 0
n = int(input("prime num"))
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print("prime number")
else:
    print("no")
    


def prime_num(x):
    c = 0
    for i in range(2,x):
        if x%i==0:
            c+=1
    
    if c>0:
        return False
    else:
        return True
   
  

def check_prime(n):
    if n==0 or n==1:
        return False
        
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
        


n = int(input("Enter num"))

if check_prime(n):
    print("yes")
else:
    print("no")

        

def fact_num(x):
    n = 1
    if x==0 or x==1:
        return 1
    for i in range(1,x+1):
        n=i*n
    return n

m = int(input("Enter num"))
print(fact_num(m))


c = 0

def testrec(x):
    global c
    c += 1
    if x== 5:
        return x
    else:
        return testrec(x+1)
    
    
y = testrec(4) 
print(y, c)


def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x * fact(x-1)
a = fact(4)
print(a)

a,b,c = 1,1,0
n = int(input("enter num"))
while True:
    a = b
    b = c
    c = a+b
    if c>n:
        break
    else:
        print(c,end=" ")
        
def armstrong(n):
    s = 0
    m=n
    while n>0:
        d = n%10
        n = n//10
        s = d**3+s
        #print(d, end=" ")
    if m==s:
        return True
    else:
        return False

y= int(input("Enter num"))
for i in range(153,x+1):
    if armstrong(i):
        print(i,end=" ")


n = int(input("Enter num"))
for i in range(n):
     if check_prime(i):
         print(i)
