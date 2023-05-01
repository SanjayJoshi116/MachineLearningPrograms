text = input('Enter a string: ')
space1 = text.find(' ')
space2 = text.find(' ',space1+1)
newtext = text[0] +'. '  + text[space1+1] +'. ' + text[space2+1] +'.'
print('New string:', newtext)