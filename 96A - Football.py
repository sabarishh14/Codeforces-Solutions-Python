n=input()
flag=0
if len(n)<7:
    flag=0
else:
    for i in range(len(n)):
        if n[i:i+7]=="0000000" or n[i:i+7]=="1111111":
            flag=1
            print("YES")
            break
if flag==0:
    print("NO")