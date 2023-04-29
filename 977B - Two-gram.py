n=int(input())
m=input()
d={}
for i in range(n):
    if m[i:i+2] not in d:
        d[m[i:i+2]]=1
    else:
        d[m[i:i+2]]+=1
ma=max(d.values())
for i in d:
    if d[i]==ma:
        print(i)
        break