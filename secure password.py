'''Generate Secure Passwords:
fixed length, At least 12 characters long is recommended, 8 at the minimum. The
combination of both upper- and lower-case letters, numbers, and symbols. Random enough that
they do not contain any predictable sequence'''


import random
l=[]
l1=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']  
out1=random.choice(l1)

l2=[chr(i) for i in range(48,58)] 
out2=random.choice(l2)

l3=[chr(i) for i in range(65,91)]
out3=random.choice(l3)

l4=[chr(i) for i in range(97,123)]
out4=random.choice(l4)

l=l1+l2+l3+l4
p=out1+out2+out3+out4

n=int(input('enter the length of password--> '))

for i in range(n-4):
    p=p+random.choice(l)

p=list(p)
random.shuffle(p)
print(*p,sep='')
