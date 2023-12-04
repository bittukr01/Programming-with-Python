a = float(input("Enter first side :"))
b = float(input("Enter second side :"))
c = float(input("Enter third side :"))
s=(a+b+c)/2
p=a*b*c
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Perimeter :",p)
print("Semi-primeter:",s)
print("Area of triangle:",area)