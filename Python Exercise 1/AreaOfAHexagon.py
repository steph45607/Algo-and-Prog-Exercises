#import math module
#to use pow and sqrt
#input will be float
#output will be float with 3 dec
#formula = ((3*sqrt(3))/2)*(pow(s,2))

import math

s = float(input("Enter the side length of the hexagon: "))

result = ((3*math.sqrt(3))/2)*(pow(s,2))

print(f"The area of a hexagon with side length {s} is ", round(result,3))