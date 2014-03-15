#Variable used to add the 'ay' on the end of the translated word.
pyg = 'ay'

#Stores user input as the original variable.
original = raw_input('Enter a word:')

#Test used to ensure that user inputs alpha characters only.
if len(original) > 0 and original.isalpha():

    #Prints original variable, stores all lower case version of original variable as word variable.
    print original
    word = original.lower()

#If the "if" conditions are not met, prints empty and program terminates.
else:
    print 'empty'
    
#Stores the first letter of word variable as first variable.
first = word[0]

#new_word variable is created by combining all characters minus the first of word variable, first variable, and pyg variable.
new_word = word[1:len(word)] + first + pyg

#Displays new_word variable.
print new_word
