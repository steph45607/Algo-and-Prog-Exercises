def calcNewHeight()->float: #will set the outcome to float data type
    cw = float(input("Enter the current width: ")) #get the current width
    ch = float(input("Enter the current height: ")) #get the current height
    dw = float(input("Enter desired width: ")) #get the desired width
    dh = (dw*ch)/cw #desired height will be equal to desired width times current height divided by current width
    print("The corresponding height is: ", dh) #print out the value

calcNewHeight()