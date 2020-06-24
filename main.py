# Write a program that asks the user for one or more sentences and then lets the user know if it is a palindrome.

name = input("Hi, please enter your name:")
print(f"\nHello, {name}!")

age = input("How old are you?: ")
age = int(age)
print(f"\nPerfect, {age}, you're old enough for this game !")

#User's Input
s= input("Please enter a sentence that can be interpreted both forewards and backwards e.g. madam, racecar.")
print(s[:]) #allows user to see what they input

#The user's input reversed
revstr=(s[: : -1])

#Check the string & deliver decision
if revstr == s: #if the string entered is the string reversed it's a palidrome
  print("Great work! You made a palindrome.")
  score = score +100
  print("Your correct score is",score)
else:
  print("This isn't a palindrome.")
score = score - 100
