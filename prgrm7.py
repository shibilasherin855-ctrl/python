a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))

if a>=b and a>=c:
   print("Biggest=",a)
elif b>=a and b>=c:
   print("Biggest=",b)
else:
   print("Biggest=",c)
