import time


"""The game consists of moving the first letter of your word, to the end,
and adding "ay" at the end """


print "Welcome to Pig Latin! I will help you changed your desired word into the translated version!"

time.sleep(2)

def translator(w):



    pyg = 'ay'  # This is the "ay" add-on
    pyg2 = 'way'  # for words that start with a vowel, no rearrangenment is made and the word "way" is added in the end

    time.sleep(0.9)

    print "Hold on while I translate this for you."

    time.sleep(0.5)

    print "***********************************"

    time.sleep(0.5)

    if len(w) > 0:

        print "You entered a valid word!"

    else:

        print "You didn't enter a word! Close the program and open it again."


    time.sleep(0.5)


    print "***********************************"

    time.sleep(0.5)


    if word.isalpha():

        print "The word doesn't contain a non-alphabetic character!"

    else:

        print "This word contains a number or a symbol. Close the program and try again"


    print "***********************************"


    if w.startswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")):

        lowercasedword = w.lower()
        translation = lowercasedword + pyg2

    else:


        lowercasedword = w.lower()
        firstletter = lowercasedword[0]
        translation = lowercasedword[1:] + firstletter + pyg


    print "Your translated word is: "

    time.sleep(1)

    print translation






word = raw_input("Enter a word: ")
translator(word)
