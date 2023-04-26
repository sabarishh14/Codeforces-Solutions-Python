n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    total = 0
    while a > 0 and b > 0:
        if a > b:
            total += a // b
            a -= (a // b) * b
        else:
            total += b // a
            b -= (b // a) * a
    print(total)
    
