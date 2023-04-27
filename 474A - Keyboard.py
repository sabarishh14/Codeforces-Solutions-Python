a="qwertyuiopasdfghjkl;zxcvbnm,./"
b=""
pos=input()
word=input()
if pos=="R":
    for i in word:
        b+=a[a.index(i)-1]
elif pos=="L":
    for i in word:
        b+=a[a.index(i)+1]
print(b)