"""for _ in range(int(input())):
    n,t=map(int,input().split())
    d=list(map(int,input().split()))
    e=list(map(int,input().split()))
    m=[[],[]]
    for i in range(n):
        if i==0:
            m[0].append(e[0])
            m[1].append(d[0])
        else:
            m[0].append(e[i])
            m[1].append(d[i]+i)
    flag=0
    
    while flag==0:
        if m[0]==[]:
            print(-1)
            break
        mx=m[0].index(max(m[0]))
        if m[1][mx]<=t:
            print(mx+1)
            flag=1
        else:
            m[0].pop(mx)
            m[1].pop(mx)"""

test = int(input())
while test:
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = -1
    for i in range(n):
        if a[i] <= t-i:
            if ans == -1 or b[i] > b[ans-1]:
                ans = i+1
    print(ans)
    test -= 1
