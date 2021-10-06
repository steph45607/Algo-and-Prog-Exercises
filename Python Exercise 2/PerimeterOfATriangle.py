#input 3 floats
#add 2 numbers and it has to be bigger than the other number
#if it's true, print the perimeter of the triangle
#ouput if true print perimeter, if false print invalid

a = float(input("Enter length of edge1: "))
b = float(input("Enter length of edge2: "))
c = float(input("Enter length of edge3: "))

if a+b>=c and b+c>=a and a+c>=b:
    print("The perimeter is ",a+b+c)
else:
    print("Perimeter cannot be calculated: the input is invalid.")