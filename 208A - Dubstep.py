a=input()
b=a.split("WUB")
while "" in b:
    b.remove("")
print(" ".join(b))