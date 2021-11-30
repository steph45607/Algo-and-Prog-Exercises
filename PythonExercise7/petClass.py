class Pet:
    def __init__(self, name = "Not provided", type = "Not provided", age = 0):
        self.__name = name
        self.__type = type
        self.__age = age
    
    def setName(self,name):
        self.__name = name
    
    def setType(self, type):
        self.__type = type
    
    def setAge(self, age):
        self.__age = age
    
    def getName(self):
        return self.__name
    
    def getType(self):
        return self.__type
    
    def getAge(self):
        return self.__age
    
    @classmethod
    def userInput(cls):
        return cls(
            input("Pet's name: "),
            str(input("Pet's type: ")),
            int(input("Pet's age: ")),
        )
    
def main():
    one = Pet()
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

    answer = str(input("You have more pets? (Y/N): "))
    if answer == "N":
        print(f"Hello I'm {one.getName()}. I'm a {one.getType()} and I'm {one.getAge()} years old.")
    else: 
        while answer == "Y":
            num = int(input("How many pets do you have in total: "))
            user = {}
            for i in range(num-1):
                print(f"Input info about pet number {i+2}.")
                user[i] = Pet.userInput()
                print("Here is the updated information about the pet:")
                print(f"Name of pet: {user[i].getName()}")
                print(f"Type of pet: {user[i].getType()}")
                print(f"Age of pet: {user[i].getAge()}")
            answer = "N"
        print("These are your pets:\n")
        print(f"Hello I'm {one.getName()}. I'm a {one.getType()} and I'm {one.getAge()} years old.")
        for i in range(num-1):
            print(f"Hello I'm {user[i].getName()}. I'm a {user[i].getType()} and I'm {user[i].getAge()} years old.")
        
main()