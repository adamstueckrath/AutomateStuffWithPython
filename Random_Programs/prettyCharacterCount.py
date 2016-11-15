
# coding: utf-8

# In[ ]:

#import pprint module
import pprint

message = input()
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)


# In[ ]:



