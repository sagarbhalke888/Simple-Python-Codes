

print("This is a quadratic equation calculator")
print("Please enter the value of a b and c to calculate the roots")
a=input("Enter the value of a and the press 'enter' key ")
b=input("Enter the value of b and the press 'enter' key ")
c=input("Enter the value of c and the press 'enter' key ")
print("Your quadratic equation is: ")
print(a,"X^2+",b,"X+",c)

a=int(a)
b=int(b)
c=int(c)
r1=(-b+pow(b*b-4*a*c,0.5))/(2*a)

r2=(-b-pow(b*b-4*a*c,0.5))/(2*a)

print("one root is ",r1)

print("other root is ",r2)
print("Yes we have calculated the roots")

