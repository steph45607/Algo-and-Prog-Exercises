from shopClassSS import ItemSS  # Import the class and the methods inside it

def itemListSS():
    # Method for mostly input user, things purchased
    items = [] # The list to store the objects created
    num = int(input("How many items will you order today?"))
    while num < 1:  # Looping to check the num value, exit loop when num is 1 or greater
        print("Number of items must be at least 1.")
        num = int(input("How many items will you order today?"))
    for item in range(num): # Looping to ask the name and amount, as much as num
        print(f"Item #{item+1}") # Starts with 1 instead of 0
        itemName = str(input("Enter food: "))
        itemAmount = float(input("Enter amount of pounds: "))
        while itemAmount <= 0:      # Looping to check the amount, exit when amount is greater than 0
            print("Amount of pounds must be greater than 0.")
            itemAmount = float(input("Enter amount of pounds: "))
        print("")
        food = ItemSS(itemName, itemAmount)     # Create the object using variables from input
        items.append(food)      # Append the object to the list
    return items    # Return the list with all the objects, later will be used for paramter assignmnets

def displaySS(theList): # Method with 1 parameter, to output the 'check'
    print("Here's a summary of the items purchased:")
    print("-------------------------------")
    for item in range(len(theList)): 
        # Looping through the objects in the list from parameter
        print(f"Item: {theList[item].getNameSS()}") # Access the name 
        print(f"Amount ordered: {theList[item].getAmountSS()} pounds") # Access the amount purchased
        print("Price per pound: ${:.2f}".format(theList[item].getItemPriceSS())) # Get a single item price
        print("Price of order: ${:.2f}".format(theList[item].calcCostSS())) # Get the total price for an item
        print("")

def totalCostSS(theList): # Method for calculating total purchased items
    total = 0 # Initial value
    for item in range(len(theList)): # Looping the calculated price for each items
        total += theList[item].calcCostSS() # Add each items total price to the total purchased
    return total


def main(): # Method to call out all 3 functions
    x = itemListSS()
    # Assign the list method to x, so can be re-used
    displaySS(x)
    print("Total cost: ${:.2f}".format(totalCostSS(x)))
    
main() # Call the function