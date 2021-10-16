import math

numer = int(input("Enter a numerator: "))
while 1==1:
    if numer <= 0:
        numer = int(input("Please re-enter the numerator. Value must be greater than 0: "))
    else:
        break

denom = int(input("Enter a denominator: "))
while 1==1:
    if denom <= 0:
        denom = int(input("Please re-enter the denominator. Value must be greater than 0: "))
    else:
        break

gcd = math.gcd(numer,denom) #find gcd value
rednumer = numer//gcd #use gcd value to reduce fraction
reddenom = denom//gcd #use gcd value to reduce fraction

if numer < denom: #proper
    print(f"{numer}/{denom} is a proper function.")
    if gcd != 1:
        print(f"This proper fraction can be reduced to: {rednumer}/{reddenom}")
    else:
        print("This proper fraction cannot be reduced any further.")
elif numer >= denom: #improper
    print(f"{numer}/{denom} is a improper function.")
    if gcd != 1:
        print(f"This improper fraction can be reduced to: {rednumer}/{reddenom}")
    else:
        print("This improper fraction cannot be reduced any further.")
    mixed = rednumer//reddenom #calculate the whole number for improper frac
    if numer%denom == 0: #to see if it's a whole number with no fraction
        print(f"The whole number is {mixed}")
    else:
        rednumer = rednumer - (reddenom*mixed) #calculate the remaining numerator in mixed fraction
        print(f"The mixed number is {mixed} and {rednumer}/{reddenom}")