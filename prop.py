def pall_num(x):
    n = str(x)
    r = n[::-1]
    if n==r:
        return True
    else:
        return False
print(pall_num(111))
    
