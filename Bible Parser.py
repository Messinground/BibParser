import urllib.request, urllib.parse, urllib.error, json, os, re
import xml.etree.ElementTree as ET


Biburl = urllib.request.urlopen('https://bereanbible.com/bsb.txt')
BibleText = str(Biburl.read()).replace('\\t','\t').split('\\n')

# Or if you are parsing from a text file:
# BibleText = open('bib.txt.', encoding="utf8").read().split('\n')
os.system("pause")

print('Type each item you would like to search for, pressing "enter" after each. Type "Done" when you are finished.')
needle = []
while 'Done' not in needle:
    needle.append(input())
needle = needle[0:len(needle)-1]

Counts = 0
References = {}

for line in BibleText:
    LineWords = line.split()
    if len(LineWords) >= 2:
        ThisRef = LineWords[0], LineWords[1]

    for Each in needle:
        while Each in line:
            Counts = Counts + 1
            References[Counts] = ThisRef

            # The following code will:
            # - Find the length of the needle
            # - Find out where the needle is in the line
            # - Remove the needle from the line (and any extra space)
            EachLen = len(Each)
            EachPos = line.find(Each)
            line = line[:EachPos].rstrip() + line[EachPos+EachLen:]
          

print(References)
print('total:',Counts)

"""
    # old code - This checks each item word by word rather than phrase by phrase
    for Each in needle:
        if Each in line:
            for word in LineWords:
                # print('checking', word)
                if Each in word:
                    Counts = Counts + 1
                    References[Counts] = ThisRef
                    # print('FOUND:',word)
            # print('Total',Counts, 'as of', ThisRef)
            # os.system("pause")
"""   
    
    
    

    


