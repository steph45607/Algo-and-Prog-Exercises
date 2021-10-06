#input mass and force
#ouput the angle of the ramp
#to measure angle (asin) use math module
#import math to access
#formula = math.asin(F/(m*g))

import math

g = 9.8
m = float(input("Enter the mass of the cart (in kg): "))
F = float(input("Enter the force to push the cart (in N): "))

formula = math.asin(F/(m*g)) 
degree = formula *(180/math.pi)

print("The anfle of the ram is", round(degree,1), "degrees")