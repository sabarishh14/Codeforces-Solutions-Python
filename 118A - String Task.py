s=input()
l=[i.lower() for i in s]
l1=[i for i in l if i not in ['a','e','i','o','u','y']]
for i in l1:
    print("."+i,end="")