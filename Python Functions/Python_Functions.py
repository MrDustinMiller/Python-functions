#0. pad right function
#build your own function to adjst the padding. take the string and add the padding to the string.
def displayPadding(unpaddedString):
    # initialising our padding variable with the size
    padding_size = 15
  
    # printing string and its length
    print ("unpadded string : ", unpaddedString)
  
    #adding padded chars into our new padded string from our old non padded string
    paddedString = "*" * (padding_size) + unpaddedString 
  
    #printing out our new padded string with our chars added to it
    print ("padded string : ", paddedString)

    #return string with padded chars
    return paddedString
            
displayPadding("Mississippi")

#1. Convert a string into a byte array. converts byte array to a hexadecimal value
def stringToByteArray():
     txt = "Onewheel"

     #encode string to bytearray with corresponding values for each character
     array1 = bytearray(txt, 'utf-16')

     #convert encoded bytearray value to hex values and print the values out
     print('Decimal values: ', array1.hex())

     #return array1

stringToByteArray()


#2. check if the strings characters are all in the alphabet, return a boolean if so
def stringIsAlpha():
    #initalize string with alphabet
    alphabet = "Mississippi Coding Academies"

    #for loop to run through each character of our string
    for char in alphabet:

        #if a character is a str return true
        if char == str:
            return bool(alphabet)

    #if every character is in the alphabet, print true to the screen. if not, print false
    print(isinstance(alphabet,str))

#stringIsAlpha()

#3. accept two strings and a integer (for the position to insert string1 into string2). return the new combined string
def stringInsert(stringOne, stringTwo, position): 
    
    #split our original stringOne into seperate substrings and store the values to splitString
    splitString = stringOne.split()

    #inserting our string two phrase into our new split string after the 3rd element position
    splitString.insert(position, stringTwo)

    #combine our splitString (still made of substrings) into one combined string
    combinedString = ' '.join(splitString)

    #print our uncombined string
    print('Our uncombined string is:', stringOne)

    #return our new combined string with both phrases together
    return print('our new combined string is:' , combinedString)

stringInsert("Hello, how are today?", "you", 3)

#4. function should accept a byte and return the corresponding char assoicated with it
def byteToChar():
    #creates a bytes object with the value 'list of bytes'
    empty_bytes = b'List of bytes'

    #generates a list of ascii character values for each letter of our bytes object
    byteCharacters = list(empty_bytes)

    #print our ascii char values to the screen
    print('Ascii char values: ', byteCharacters)

    #returns ascii values
    return byteCharacters
byteToChar()

#5. should accept a char and an int. should then return a string made of that char repeated the number of times specified by the int
def stringRepeatFromChr(char, repeatNum):

    #empty string to fill with our repeated chars
    repeatedChars = ""

    #increment counter for out while loop
    count = 0

    #while loop to run based on our count variable
    while count <= 0:
        #take our char parameter passed into the function and multiply it by repeatNum (which is also passed into the function as a parameter)
        #store the new string with repeating chars to variable repeatedChars
        repeatedChars += char * repeatNum

        #print result to screen of our new string
        print('Our repeated char: ', repeatedChars)

        #incremet our count so the loop stops
        count += 1

#calling our function with two arguments to be passed into the function
stringRepeatFromChr('x', 10)

#6. should accept an array of strings, and a char. Then return a string made from each string in the array joined by the char given
def stringCombine(stringArray, char):
    #setting a new variable newString to the value of stringArray
    newString = stringArray

    #finds the length of the list and floor divides (divides two nums and rounds down) the length by 2
    #colon operator allows us to access first half/second half of list
    splitStringOne = newString[:len(newString)//2]
    splitStringTwo = newString[len(newString)//2:]

    #adding our given char to our first half of the list
    splitStringOne += char

    #adding the second half of the list back to the first half with our char joining the two alfs
    splitStringOne += splitStringTwo

    #return our new string
    return print('our joined string with our char is: ', splitStringOne)

stringCombine(["Dustin", "Samuel", "Miller"], "*")

#7. should accept a string and return a string with the characters randomly shuffled.
def stringMix(stringOne):
    #importing random module
    import random

    #assinging the string "programming" to variable unshuffled
    unshuffled = stringOne

    #print out the original, unshuffled string to the screen
    print("Original string: " + unshuffled)

    #make new variable for our shuffled string. Assigns formatting to the string once outputted
    shuffled = []

    #assings our unshuffled string value to the variable shuffled. Slices the string (colon is a slicing operator) from index 0-10 
    shuffled [:] = unshuffled

    #from imported random module. the shuffle function will take a sequence (our shuffled variable in this case) and rearrange the elements
    random.shuffle(shuffled)

    #return our new, shuffled variable
    return print('shuffled string: ', shuffled)
stringMix("Programming")

#8. should accept a string and return an uppercase version of the string.
def toUpper():
    #take user input
    stringOne = "mississippi"

    #print non uppercase string out first
    print('our lowercase string is', stringOne) 

    #convert the users input to uppercase
    stringOne = stringOne.upper()

    #return userInput with all uppercase letters
    return print('our uppercased string is:', stringOne)

toUpper()

#9. should accept a string and return alower case version of the string.
def toLower():
    #take user input
    stringOne = 'MISSISSIPPI'

    #print our capatailzed string to the screen
    print('Our capatilized string is', stringOne) 

    #convert the users input to uppercase
    stringOne = stringOne.lower()

    #return userInput with all uppercase letters
    return print('our lowercase string is:', stringOne)

toLower()

#10. should accept a char and return the integer index of the first occurrence of the char within the string. If the char is not in the 
#string the function should return -1.
def stringCharIndex(stringOne, char):
    #counter to control whether our char is in our string or not. needed for our if statements below
    count = 0

    #print our string to the screen so user can see the info theyre working with
    print("Our string is:", stringOne)

    #for loop to iterate every character in our string. our if statement in our for loop determines if a character in the string is equal to our given char
    for i in range(len(stringOne)):
        if(stringOne[i] == char):
            count = 1
            break

    #if count is equal to one that means our char was in our string. display the position of the first occurence. if char not in string, return -1
    if (count == 1):
        print ("The first occurence of our char 'e' is found at position", i)
    else:
        return -1
    
stringCharIndex("lime green", "e")

#11. should accept a string and return a reversed version of that string.
def stringReverse(unreversedString):
    #empty string to hold our string once its reversed
    reversedString = ""

    #print our normal unreversed string to the screen
    print('our unreversed string is: ', unreversedString)
    #slice our string but with no given start or end value. it will automatically start from 0 and go to the end of the string.
    #-1 is a step value and tells us that it needs to be traversed in a reversed manner.
    unreversedString = unreversedString[::-1]

    #assign our empty reversed string the value of the unreversedString
    reversedString += unreversedString

    #return our new, reversed string
    return print('our reversed string is: ', unreversedString)

stringReverse("Aquafina")

#12. should accept a string and an int, then return the string repeated the number of times specified by the int.
def stringRepeat(unrepeatedString, repeatNum):
    #assign a new variable 'repeatedString' the value of our unrepeatedString and multiply it by our repeatNum which will hold the value '10'
    repeatedString = unrepeatedString * repeatNum

    #return our new repeated string
    return print('our repeated string is: ', repeatedString)

stringRepeat("Coding", 10)

#13.should accept a string and a bool. The bool controls if y is considered a vowel or not. The function should return an int indicating how many 
#vowels the string contains.
def stringVowelCount(stringOne, boolTest):
    #declare our vowel variable and intialize its value to empty
    vowel = ' '
    
    #declare our vowelCount variable and intialize its value to 0
    vowelCount = 0

    #declare our boolean variable and set its value to True
    boolTest = True

    #print to the screen 
    print('Our string contains the words:', stringOne)

    #our bool controls if y is considered a vowel or not. tests the condition and sets the value of vowel to 'y' if true, 'aeiou' if false.
    if boolTest == True:
        vowel = 'y'
    elif boolTest == False:
        vowel = 'aeiou'

    #for loop runs through our string and determines if each letter is a vowel or not, if equal add 1 to our vowelcount each time
    for i in stringOne:
        if (i == 'y' or i == 'Y' or i == 'e' or i == 'E' or i == 'a' or i == 'A' or i == 'i' or i == 'I' or i == 'o' or i == 'O'
            or i == 'u' or i == 'U'):
            vowelCount += 1     
    return print('The total number of vowels in this string is = ', vowelCount)       
        
stringVowelCount('amethyst, abyss, You, Yall, anyway, Yeet, yeah', bool)

#14. accepts a string and returns a bool indicating if the string passed can be considered a strong password. 
def passwordStrong(password):
    #bool will indicate if our string can be considered a strong password
    boolTest = True

    #variable holds the criteria for all of our special characters
    specialChar = '!,@,#,$,%,'

    #if statements to check the criteria of a strong password so it can be compared to the password passed into the function, the criteria is:
    #atleast 8 characters long/no more than 20 long
    #atleast one number 
    #atleast one lowercase letter
    #atleast one uppercase letter
    #atleast one special character
    if len(password) < 8:
        print('Your password should be at least 8 characters long')
        boolTest = False
    if len(password) > 20:
        print('Your password cannot be longer than 20 characters')
        boolTest = False
    if not any(char.isdigit() for char in password):
        print('Your password should contain at least one numeral')
        boolTest = False
    if not any(char.islower() for char in password):
        print('Your password sould contain atleast one lowercase character')
        boolTest = False
    if not any(char.isupper() for char in password):
        print('Your password should contain atleast one uppercase character')
        boolTest = False
    if not any(char in specialChar for char in password):
        print('Your password should contain atleast one special character')
        boolTest = False
    if boolTest:
        return print('is this password okay?', boolTest)

passwordStrong("Mississippi2!")

#15. accepts an array of doubles and returns the sum of the values in the array.
def arraySum(arrayOne):
    #varaible to store the sum of our array 
    sumOfArray  = 0
      
    #iterate through the array and add each element of our array to the variable sumOfArray
    for i in arrayOne:
        sumOfArray = sumOfArray + i

    #return the new value stores in sumOfArray (which is the sum of each element in the array)      
    return print('The sum of our array is', sumOfArray)  
  
#display sum 
arraySum([23, 56, 78, 42])

#16. function accepts an array of doubles and returns the mean of the values in the array.
def arrayMean(arrayOne):
    #variable to store the mean of our array
    meanOfArray = 0

    #variable to store the sum of our array
    sumOfArray = 0

    #for loop to run through the index of our array and add the sum of our array to the variable sumOfArray
    for i in arrayOne:
        sumOfArray = sumOfArray + i
    
    #intialize our arrayLength variable with the value of the length of our arrayOne
    arrayLength = len(arrayOne)

    #declare/intialize our meanOfArray variable. our sumOfArray gets divded by the length of the array, and the value gets stored to meanOfArray
    meanOfArray = sumOfArray / arrayLength

    #return our mean value from our array
    return print('The mean of our array is', meanOfArray)
    
#display mean
arrayMean([78,65,34,65])
