u,l,v,c,a = 0,0,0,0,"aeiou"
s = input("Enter string")
for i in s:
    if i.isalpha()==True:
        if i.islower()==True:
            l+=1
        else:
            u+=1
        if i in a:
            v+=1
        else:
            c+=1
print(f"vowel {v}\nconsonent {c} \nupper {u} \nlower {l}")         
            

