pyg = 'ay'
#Variable used to add the 'ay' on the end of the translated word.

original = raw_input('Enter a word:')
#Stores user input as the original variable.

if len(original) > 0 and original.isalpha():
#Test used to ensure that user inputs alpha characters only.

    print original
    word = original.lower()
    #Prints original variable, stores all lower case version     of original variable as word variable.

else:
    print 'empty'
    #If the "if" conditions are not met, prints empty and         program terminates.
    
first = word[0]
#Stores the first letter of word variable as first variable.

new_word = word[1:len(word)] + first + pyg
#new_word variable is created by combining all characters minus the first of word variable, first variable, and pyg variable.

print new_word
#Displays new_word variable.