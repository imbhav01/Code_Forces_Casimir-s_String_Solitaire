x = int(input())
for i in range(0,x):
    y = str(input())
    z = []
    a,b,c = 0,0,0
    for i in range(0,len(y)):
        z.append(y[i])
    
    for i in z:
        if i == "A":
            a+=1
        elif i == "B":
            b+=1
        else:
            c+=1
        
    if a+c == b:
        print("YES")
    else:
        print("NO")
            