a = int(input("first number:"))
b = int(input("second number:"))

print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")

c = int(input("enter choice"))

if c==1:
        print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print("invalid")
