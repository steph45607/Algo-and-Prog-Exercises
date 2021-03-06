class ItemSS:
    def __init__(self, foodName, amount):
        self.__foodName = foodName
        self.__amount = amount
        self.__itemPrice = self.getItemPriceSS()
        self.__calcPrice = self.calcCostSS()

    def getNameSS(self): 
        # To return the name variable, since it' private
        return self.__foodName
    
    def getAmountSS(self):
        # To return the amount, since it's private
        return self.__amount
    
    def getItemPriceSS(self):
        # To return single item's price, since it's private
        self.__PriceListSS()
        return self.__itemPrice
        """
        """

    def __PriceListSS(self):
        # Will match the input name with the price
        if self.__foodName == "Dry Cured Iberian Ham":
            self.__itemPrice = 177.80
        elif self.__foodName == "Wagyu Steaks":
            self.__itemPrice = 450.00
        elif self.__foodName == "Matsutake Mushrooms":
            self.__itemPrice = 272.00
        elif self.__foodName == "Kopi Luwak Coffee":
            self.__itemPrice = 306.50
        elif self.__foodName == "Moose Cheese":
            self.__itemPrice = 487.20
        elif self.__foodName == "White Truffles":
            self.__itemPrice = 3600.00
        elif self.__foodName == "Blue Fin Tuna":
            self.__itemPrice = 3603.00
        elif self.__foodName == "Le Bonnotte Potatoes":
            self.__itemPrice = 270.81
        else: # If the item doesn't exist
            self.__itemPrice = 0
        
    def calcCostSS(self):
        # To calculate the price for an amount of item bought
        self.__calcPrice = self.__itemPrice * self.__amount
        # Item price times amount bought
        return self.__calcPrice
        # Return to access it later