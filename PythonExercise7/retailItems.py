class Retail_Item:
    def __init__(self, type, amount, price):
        self.__type = type
        self.__amount = amount
        self.__price = price

    def getType(self):
        return self.__type
    
    def getAmount(self):
        return self.__amount

    def getPrice(self):
        return self.__price

    def __str__(self): # Do the formating with whitespaces
        return f"{self.getType().ljust(20)}{str(self.getAmount()).ljust(13)}${str(self.getPrice())}"
    
    @classmethod # So I can ask the user if they want to make multiple object, class as object factory
    def userInput(cls):
        return cls(
            str(input(f"Name of item {i+1}: ")), # i+1 to display number from 1 not 0
            int(input(f"Amount of item {i+1}: ")),
            float(input(f"Price of item {i+1}: "))
        )
        
def main():
    num = int(input("How many items do you want to buy?")) # To determine iteration
    items = {} # Store data
    global i # Make this global so the userInput method can access it too, as indexing
    for i in range (num): # Iterate to number of items you want to input / buy
        items[i] = Retail_Item.userInput()
    print("\n")
    print("Here is the summary of the items you added:")
    print("Item             Amount           Price")
    print("----------------------------------------")
    for i in range(num): # Iterate as much as the items bought
        print(items[i].__str__())
    total_price = 0
    for i in range(num):
        total_price += items[i].getPrice() * items[i].getAmount()
    print(f"Total price: .ljust(33) ${total_price}")