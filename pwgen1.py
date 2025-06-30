import random
#Used for a random generation of characters

uppercaseLetter1=chr (random.randint(65,90))
uppercaseLetter2=chr (random.randint(65,90))
uppercaseLetter3=chr (random.randint(65,90))
uppercaseLetter4=chr (random.randint(65,90))
uppercaseLetter5=chr (random.randint(65,90))
uppercaseLetter6=chr (random.randint(65,90))
#Variables for uppercase letter minimum

lowercaseLetter1=chr (random.randint(97,122))
lowercaseLetter2=chr (random.randint(97,122))
lowercaseLetter3=chr (random.randint(97,122))
lowercaseLetter4=chr (random.randint(97,122))
lowercaseLetter5=chr (random.randint(97,122))
lowercaseLetter6=chr (random.randint(97,122))
#Variables for lowercase letters

digit1=chr (random.randint(48,57))
digit2=chr (random.randint(48,57))
digit3=chr (random.randint(48,57))
digit4=chr (random.randint(48,57))
digit5=chr (random.randint(48,57))
digit6=chr (random.randint(48,57))
#Variables for digits/numbers

specialChar1=chr (random.randint(33,63))
specialChar2=chr (random.randint(33,63))
specialChar3=chr (random.randint(33,63))
specialChar4=chr (random.randint(33,63))
specialChar5=chr (random.randint(33,63))
specialChar6=chr (random.randint(33,63))
#Variables for special char

password = lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + lowercaseLetter6 + uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + specialChar1 + specialChar2 + specialChar3 + specialChar4
#var putting it all together

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
#Building func for the shuffle.  This accomplishes this by turning a string into a list so it can be changed and randomized then back into a string

password = shuffle(password)
print(password)
#printing the output for personal use

"""things to add over time
changing out the 'import random' to 'import secrets'
user input to determine how long they want the password to be
whether they require special characters
saving the password into an encrypted file with a label for what it was used for
introducing a GUI element and master password required for access
"""