def calc(x):
    maxv = x % 10
    minv = x % 10
    while x:
        maxv = max(maxv, x % 10)
        minv = min(minv, x % 10)
        x = x // 10
    return maxv - minv

def solve():
    l, r = map(int, input().split())
    ans = 0
    v = -1
    for i in range(l, r+1):
        temp = calc(i)
        if temp > v:
            ans = i
            v = temp
            if v == 9:
                break
    print(ans)

T = int(input())
for _ in range(T):
    solve()