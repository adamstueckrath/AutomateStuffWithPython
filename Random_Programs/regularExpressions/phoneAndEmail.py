
# coding: utf-8

# In[ ]:

#! python 3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipbaord.

import pyperclip, re

# create phone regex
phoneRegex = re.compile(r'''(
                (\d{3}|\(\d{3}\))?            # area code
                (\s|-|\.)?                    # separator: character can be space (\s), hyphen (-), or period(.)
                (\d{3})                       # first 3 digits
                (\s|-|\.)                     # separator
                (\d{4})                       # last 4 digits
                (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                )''',re.VERBOSE)

# create email regex
emailRegex = re.compile(r'''(
                [a-zA-Z0-9._%+-]+   # username
                @                   # @symbol
                [a-zA-Z0-9.-]+      # domain name
                (\.[a-zA-Z]{2,4})   # dot-something
                )''',re.VERBOSE)

# find matches in clipboard text
text = str(pyperclip.paste()) # get the string on the clipboard
matches = []

for groups in phoneRegex.findall(text): # the findall() regex will return a list of tuples
    phoneNum = '-'.join([groups[1],groups[3], groups[5]]) # instead of groups[0], make all numbers the same format
    if groups[8] != '': 
        phoneNum += ' x' + groups[8] # format number extension 
    if phoneNum not in matches:
        matches.append(phoneNum) # append number to matches
    else:
        continue

for groups in emailRegex.findall(text):
    if groups[0] not in matches:
        matches.append(groups[0]) # append email to matches
    else:
        continue

# copy reuslt to clipboard 
if len(matches) > 0: # if matches found, copy to clipboard and print
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

