def days(hours, mins, secs):
    day = (hours/24)+((mins/60)/24)+(((secs/60)/60)/24) #calculate the value of day

    print("The number of days is:",round(day,4)) #round() round to 4 decimal places

def convertToDays():
    hours = float(input("Enter number of hours: "))
    mins = float(input("Enter number of minutes: "))
    secs = float(input("Enter numbers of seconds: "))

    days(hours, mins, secs) #run days() after knowing hours, mins, secs values

convertToDays() #run convertToDays() to initial the input