
# coding: utf-8

# In[7]:

#! python3
# bulletPointAdder.py - Adds wkikpedia bullet points to the start 
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)


# In[ ]:

**'Lists of animals\nLists of aquarium life\nLists of biologists by author
abbreviation\nLists of cultivars'

