"""The game consists of moving the first letter of your word, to the end,
and adding "ay" at the end """


print "Welcome to Pig Latin! I will help you changed your desired word into the translated version!"

word = raw_input('First, enter the word: ') #takes word from user

pyg = 'ay' #This is the "ay" add-on

if len(word) > 0:

    print "You entered a valid word!"

else:

    print "You didn't enter a word! Close the program and open it again."



if  word.isalpha():

    print "The word doesn't contain a non-alphabetic character!"

else:

    print "This word contains a number or a symbol. Close the program and try again"
