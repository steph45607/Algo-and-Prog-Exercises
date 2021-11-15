import os

def count(file): # make the function
    sumWord = 0 # intialize for counting and storing later -> the length of all words
    numWord = 0 # initialize for counting and storing later -> the number of words
    with open(file,'r') as book: # use with, safer ( in case forgot close )
        for words in book: # looping to access line in file
            word = words.split() # split the lines to words
            for i in range(len(word)): # looping to count
                sumWord += len(word[i]) # sum up the length of all the words
                numWord += 1 # sum up all the number of words
        avg = sumWord/numWord # average formula
        return avg # so can store value
    

print(count("Kafka.txt"))