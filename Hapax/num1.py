import os
import string

os.chdir('/Users/steph/Desktop')
book  = open('Kafka.txt','r')
kafka = book.read().lower().replace("\n"," ")

def theHapax(theBook):
    replace =""
    for things in theBook:
        if things not in string.punctuation:
            replace += things
    theBook = replace
    wordlist = theBook.split(" ")

    # check the word, so wont check the same word over n over again
    allList = {}

    for text in wordlist:
        if text not in allList:
            allList[text] = 1
        else:
            allList[text] += 1

    hapax = []

    for text in allList:
        if allList[text] == 1:
            hapax.append(text)

    print(hapax)

theHapax(kafka)
