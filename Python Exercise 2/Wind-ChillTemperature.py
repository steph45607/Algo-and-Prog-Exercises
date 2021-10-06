#use while as a looping
#if condition is wrong, repeat loop, if right stop looping
#ask for new question

score = False

ta = int(input("Enter the temperature in Fahrenheit: "))

while score == False:
    if(ta<=41 and ta>=-58):
        score = True
        v = int(input("Enter the wind speed miles per hour: "))
    else:
        score = False
        print("Temperature must be between -58F and 41F")
        ta = int(input("Please re-enter the temperature in Fahrenheit: "))

while score == True:
    if(v>=2):
        score == False
        twc = 35.74 + (0.6215*ta) - (35.75*pow(v,0.16)) + 0.4275*ta*pow(v,0.16)
        print("The wind chill index is %2.3f" % (twc))
        break
    else:
        score == True
        print("Speed must be greater than or equal to 2")
        v = int(input("Please re-enter the wind speed miles per hour: "))