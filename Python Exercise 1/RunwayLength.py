#acceleration a
#speed v
#formula (v**2)/(2*a)
#output formula

v = int(input("Enter the plane's take off speed n m/s: "))
a = float(input("Enter the plane's acceleration in m/s**2: "))
formula = (v*v)/(2*a)

print("The minimum runway length needed for this airplane is %2.4f meters." % (formula))