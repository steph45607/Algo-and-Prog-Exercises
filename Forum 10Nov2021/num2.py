import os

# os.chdir('/Users/steph/Algo-and-Prog-Exercises/Forum 10Nov2021/')
# i dont use this, bc wanna make function

def writeTxt(readText,writeText):  # function, ask for the text you want to read and write
    file = open(readText, 'r') # open the file you wan to read
    file2 = open(writeText, 'w') # open the file you want to write

    count = 0 # initialize
    for line in file: # looping through the lines
        count += 1 # increment 1 count var, to be printed later
        file2.write("{}:{}".format(count,line)) # print the line with format count : line

    file.close() # close read text
    file2.close() # close write text

writeTxt("text.txt","text2.txt") # run the function