#variable creation and assigning a value to a specific value 
st_Word = "Spam"
nd_Word = "and"
rd_Word = "eggs"
space = " "

#first method I can use to pint out my items using VARIABLE NAMES (vars CONCATINATION)
print st_Word + space + nd_Word + space + rd_Word

#second method I can use to print out my using the exact string concatination
print "Spam"+" "+"and"+" "+"eggs"
#using third method to print out numbers as strings
amount = 56
print "Spam"+" "+"and"+" "+"eggs" +" "+"overall amount"+" "+ str(amount)
"""using fourth method to print out using exact strings and variable names with modulo (%) operator to print next variable that comes after the first variable"""

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'This a silly %s." % (string_1, string_2)
#similer to what I've just done

name = raw_input("What is your name?")
surname = raw_input("What is your surname?")
DoB = raw_input("and your date of birth?")
#agan here I used modulo sign as the string's place holder
print "Hello %s %s.Is this the year you were born %s" % (name, surname ,str(DoB))
if name == "oyama":
	print ("make sure you put a valid name!")
elif surname == "Siphula":
	print ("You really know me")
else:
	print "Now let's prepare for the game take a BREATH !!!"

answer = "YES"
toBegin = "Are you ready ?"

while True:
 
    start = str(raw_input(toBegin))

    if start == answer:
	print ("You are not ready. Try again !!!")
    else: # start == answer
	print ("Go !!!")
	break

print ("Now let's play the guessing game!")

answer = 23
question = "What number am I thinking of? "
while True:
    guess = int(input(question))

    if guess < answer:
        print ("Little higher")
    elif guess > answer:
        print ("Little lower")
    else: # guess == answerOne
        print ("MINDREADER!!!")
        break

"""Lets know your info then """
name = raw_input("What is your name?") #almost like to alert function and take the variable assign it from my input 
quest = raw_input("What is your quest?") #almost like to alert function and take the variable assign it from my input 
color = raw_input("What is your favorite color?") #almost like to alert function and take the variable assign it from my input 

print "Ah, so your name is %s, your quest is %s, printing out"
"and your favorite color is %s ." % (name, quest, color) #%s's to replace the inputs by also using a modulo-% then to result in a full sentence
