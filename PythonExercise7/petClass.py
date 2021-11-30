class Pet:
    def __init__(self, name = "Not provided", type = "Not provided", age = 0):
        self.__name = name
        self.__type = type
        self.__age = age
    
    def setName(self,name): # Setter for name
        self.__name = name
    
    def setType(self, type): # Setter for type 
        self.__type = type
    
    def setAge(self, age): # Setter for age
        self.__age = age
    
    def getName(self): # Getter for name
        return self.__name
    
    def getType(self): # Getter for type
        return self.__type
    
    def getAge(self): # Getter for age
        return self.__age
    
    @classmethod # Using class as a factory
    def userInput(cls): # Function to get object from user input
        return cls(
            input("Pet's name: "), # Get pet name from user input
            str(input("Pet's type: ")), # Get pet type from user input
            int(input("Pet's age: ")), # Get pet age from user input
        )

def main(): # To ask from user
    one = Pet() # Initial pet obj
    print("A pet object has been created. Here is the initial information about the pet:")
    print(f"Name of pet: {one.getName()}")
    print(f"Type of pet: {one.getType()}")
    print(f"Age of pet: {one.getAge()}")
    print("Let's update the information for a pet!")
    oneName = str(input("Enter the pet's name: "))
    oneType = str(input("Enter the type of animal: "))
    oneAge = int(input("Enter the pet's age: "))
    one.setName(oneName)
    one.setType(oneType)
    one.setAge(oneAge)
    print("Here is the updated information about the pet:")
    print(f"Name of pet: {one.getName()}")
    print(f"Type of pet: {one.getType()}")
    print(f"Age of pet: {one.getAge()}")

    answer = str(input("You have more pets? (Y/N): ")) # Ask if they have more pets
    if answer == "N": # If no, program ends with desc of initial pet
        print(f"Hello I'm {one.getName()}. I'm a {one.getType()} and I'm {one.getAge()} years old.")
    else:  # If yes, will ask this
        while answer == "Y":
            num = int(input("How many pets do you have in total: ")) # The total pets
            user = {} # To store obj based on numbers
            for i in range(num-1): # Iterate the object creation process
                print(f"Input info about pet number {i+2}.")
                user[i] = Pet.userInput() # Declaration of object
                print("Here is the updated information about the pet:")
                print(f"Name of pet: {user[i].getName()}")
                print(f"Type of pet: {user[i].getType()}")
                print(f"Age of pet: {user[i].getAge()}")
            answer = "N" # After iteration, while loop will end with this
        print("These are your pets:\n") # Print a short desc of pets
        print(f"Hello I'm {one.getName()}. I'm a {one.getType()} and I'm {one.getAge()} years old.")
        for i in range(num-1): # Iterate to make multiple pet desc
            print(f"Hello I'm {user[i].getName()}. I'm a {user[i].getType()} and I'm {user[i].getAge()} years old.")
 