"""n,k=map(int,input().split())
l=[i for i in range(1,n+1)]
l2=[i for i in l if i%2!=0]
l3=[i for i in l if i%2==0]
l=l2+l3
print(l[k-1])"""

n, k = map(int, input().split())
if k <= (n + 1) // 2:
    print(k * 2 - 1)
else:
    print((k - (n + 1) // 2) * 2)