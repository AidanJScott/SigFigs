'''
Signigicant Figures (chemistry) Rules:

all nonzero digits are significant
leading zeros before a decimal (left to right) are not significant
trailing zeros after the first nonzero digit are significant IF there is a decimal
'''

def main():
    numberValid = False
    negativeValue = False
    decimalValue = False

    #send to validity checking function
    while numberValid == False:
        number = input("Enter a valid number (only digits 0-9 and one decimal): ")
        numberValid = numValid(number)

    #send to list converter function
    numberList = listConvert(number)

    #account for negative numbers
    if numberList[0] == "-":
        stripList = numberList[1:]
        negativeValue = True
        
    else:
        stripList = numberList

    #check for a decimal using the length of entered string
    if "." in numberList:
        decimalValue = True

    #convert list into a form without any decimals by sending to function
    if decimalValue == True:
        finalList = decimalInput(stripList)

    #calculate significant figures based on
    #remaining list stripped of negatives and decimals    
    if decimalValue == False:
        finalList = integerInput(stripList)

    #finalList contains only the significant digits        
    sigFigs = len(finalList)

    print("\nThe entered value has", sigFigs, "significant digit(s)")

    number = float(number)
    print(f"\nThe entered value in scientific notation: {number:.{sigFigs-1}E}")
    
    return



def decimalInput(stripList):
    #initialize list
    deciList = [0] * (len(stripList)-1)
    
    #find the index of the decimal and delete it from the list    
    deciIndex = stripList.index(".")

    deciList = stripList[:deciIndex] + stripList[(deciIndex + 1):]

    #check for the index of the first nonzero digit
    foundNonzero = False
    count = 0

    #loop checks for nonzero digit
    while foundNonzero == False:
        if (count != (len(deciList)-1)):

            if deciList[count] == "0":
                count += 1 
            else:
                foundNonzero = True
    
    #strip the list one final time for nonzero digits
    finalList = deciList[count:]    

    return finalList


def integerInput(stripList):
    foundFNonzero = False
    foundLNonzero = False
    countFirst = 0
    countLast = 0
    
    #loop checks for first nonzero digit
    while foundFNonzero == False:
        if countFirst != (len(stripList)-1):

            if stripList[countFirst] == "0":
                countFirst += 1 
            else:
                foundFNonzero = True

    #reverses list to find trailing zeros
    revStripList = stripList[::-1]
    

    #loop checks for last nonzero digit
    while foundLNonzero == False:
        if countLast != (len(revStripList)-1):

            if revStripList[countLast] == "0":
                countLast += 1 
            else:
                foundLNonzero = True
    if countLast == 0:
        finalList = stripList[countFirst:]

    else:
        finalList = stripList[countFirst:(-(countLast))]
        
    return finalList


#iterate over the string and turn it into a list for manipulation
def listConvert(number):
    numberList = [0] * len(number)
    
    for count in range(len(number)):
        numberList[count] = number[count]

    return numberList


def numValid(number):
    redo = False
    #account for non-numerical characters or too many decimals
    try:
        number = float(number)

        if number == 0.0:
            raise ValueError

    except ValueError:
        print("\n***Number must not be 0 and only contain digits with a single decimal***\n")
        numberValid = False
        redo = True

    if type(number) is float and redo != True:
        numberValid = True

    return numberValid

main()
