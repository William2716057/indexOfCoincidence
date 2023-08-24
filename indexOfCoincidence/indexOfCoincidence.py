#Will tell the likelyhood that a text is a substituted cipher or random text
#May also be used to identify the likely languaged that was encoded

import collections 

def IndexOfCoincidence(text):
    #remove all spaces and capitalise text
    text = text.replace(" ", "").upper()

    #calulate the length of the text without spaces
    length = len(text)
    #create dictionary to be used in function
    counts = collections.Counter(text)

    ioc = 0
    for letter in counts:
        frequency = counts[letter]
        #to make calculation the frequency of each letter is multiplied by the frequency of each letter minus 1 
        #then divided by the length of the text multiplied by the length minus 1
        ioc += (frequency * (frequency -1)) / (length * (length - 1))

    return ioc

if __name__ == "__main__":
    inputText = input("Paste text here: ")
    result = IndexOfCoincidence(inputText)
    print(f"Index of coincidence = {result}")




