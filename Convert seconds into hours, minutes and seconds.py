a= int(input("enter seconds:"))

hr = a//3600
mi = (a%3600)\\60
sec = a%60

print("hours:",hr)
print("minutes:",mi)
print("seconds:",sec)
