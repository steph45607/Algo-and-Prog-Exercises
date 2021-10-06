# q <10  no disc
# q 10-19 10% disc
# q 20-49 20% disc
# q 50-99 30% disc
# q >=100 40% disc
# input quantity
# output discount amount
# output discounted total

q = int(input("Enter the number of packages purchased: "))
subtotal = 99*q
if q < 10:
    disc = 0
elif q >= 10 and q <= 19:
    disc = 10
elif q >= 20 and q <= 49:
    disc = 20
elif q >= 50 and q <= 99:
    disc = 30
elif q >= 100:
    disc = 40

discAmnt = subtotal * (disc/100)

print(f"Discount Amount @ {disc}% : $ ""{:.2f}".format(discAmnt))

total = subtotal - discAmnt

print("Total Amount: $ {:.2f}".format(total))