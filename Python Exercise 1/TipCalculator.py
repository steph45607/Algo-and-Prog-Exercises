#input the subtotal
#input tip percent
#output subtotal with 2 dec
#output tip in dollars with 2 dec
#total subtotal and tip in dollars with 2 dec

subtotal = float(input("Enter the subtotal: $"))
tipPerc = float(input("Enter tip amount(as a %): "))

tip = (subtotal*(tipPerc/100))
total = tip +subtotal

print("Subtotal: ${:,.2f}".format(subtotal))
print("Tip: ${:,.2f}".format(tip))
print("Total: ${:,.2f}".format(total))