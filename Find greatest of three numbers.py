a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a>b>c:
    print("a is greatest")
elif b>a>c:
    print(" b is greatest")
elif a>c>b:
    print("a is greatest")
elif b>c>a:
    print("b is greatest")
elif c>a>b:
    print("c is greatest")
else:
    print("c is greatest")

