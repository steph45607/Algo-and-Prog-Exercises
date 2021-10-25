def celcius(f): #function to change f to c
    return (5/9)*(f-32)

def kelvin(c): #function to change c to k
    return c +273.15

def convert_temp():
    f = int(input("Enter a temperature in Fahrenheit: ")) #to get value f
    print("The temperature in Fahrenheit is: ",f)
    c = celcius(f) #convert f to c
    k = kelvin(c) #convert c to k
    print("The temperature in Celcius is: ",c)
    print("The temperature in Kelvin is: ",k)

convert_temp() #call the function