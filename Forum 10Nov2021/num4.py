import os
import re # using regex

def splitter(text,writeText):  # function, ask for the text you want to read and write
    file = open(text, 'r') # open the file you wan to read
    file2 = open(writeText,'w') # file you want to write
    for line in file: # looping through the file to read
        cut = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s",line) # use regex to "Set the rules"
    for i in range(len(cut)): # loop to print lines
        file2.write(cut[i]) # print the line
        file2.write("\n") # make a new line
    
    file.close() # close read text
    file2.close() # close write text

splitter("miyagi.txt","new.txt")