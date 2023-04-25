n=int(input())
co=0
for i in range(n):
    s=input()
    si=s.split()
    c=si.count('1')
    if c >= 2:
        co+=1
print(co)