#Write a program that asks the user for one or more sentences 

import re 
#Getting info from user
#Question1
def get_test_username():  
  name = input('Please enter your name  ')
  print(name)
  if name == name[::-1]:
    print(name, 'is a palindrome.')
  else:
    print(name,'is not a palindrome.')


#Question2
def get_test_num():
  num = input('Enter your age  ')
  print(num)
  if num == num[::-1]:
    print(num, 'is a palindrome.')
  else:
    print(num,'is not a palindrome.')

#Question3
def get_phrase():
  word = input('Enter a word of phrase  ')
  #The next line wipes the punctuation from the string. This will strip the string
  cleaned_phrase = re.sub(r'[^A-Za-z]', '', word.lower())

  print(cleaned_phrase)
  print(word)
  #This tests the stripped string by reversing the user input
  if cleaned_phrase == cleaned_phrase[::-1]:
    print(word, 'is a palindrome.')
  else:
    print(word,'is not a palindrome.')
#This function will call the test for each 
def get_tests():
  print ('Hello!')
  get_test_username()
  get_test_num()
  get_phrase()

get_tests()

#Checks conditions and test for palindrome or no..
#if 
  #print('This is a palindrome.')
#elif:  WHY WON'T ELIF WORK
  #print('This is not a palindrome.')bomb
#String Hash? 

#WORD CHECK...Bob, 44, Sharetta, Tonya, Michael

  #Figure out how to make a single condition that applies to all



# Write a program that asks the user for one or more sentences and then lets the user know if it is a palindrome.

#name = input("Hi, please enter your name:")
#print(f"\nHello, {name}!")

#age = input("How old are you?: ")
#age = int(age)
#print(f"\nPerfect, {age}, you're old enough for this game !")

#User's Input
#s= input("Please enter a sentence that can be interpreted both forewards and backwards e.g. madam, racecar.")
#print(s[:]) #allows user to see what they input

#The user's input reversed
#revstr=(s[: : -1])

#Check the string & deliver decision
#if revstr == s: #if the string entered is the string reversed it's a palidrome
#  print("Great work! You made a palindrome.")
#  score = score +100
#  print("Your correct score is",score)
#else:
#  print("This isn't a palindrome.")
#score = score - 100

# Simple String Palindrome

#string = input("enter the string:")
#rev_string = string[::-1]
#if string == rev_string:
#  print("string is palindrome")
#else:
#  print("string is not palindrome") 

# Simple Integer Palindrome
 #no slice method for the integer number

#number = int(input("enter the number:"))
#string = str(number)
#rev_string = string[::-1]
#print ("reversed string:",rev_string)
#if string == rev_string:
#  print("number is palindrome")
#else:
#  print("number is not palindrome")