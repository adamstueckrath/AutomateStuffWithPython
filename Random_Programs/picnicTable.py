
# coding: utf-8

# In[ ]:

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth, '.')+ str(v).rjust(rightWidth))


# In[ ]:

#test
picnicItems = {'sandwhiches':4, 'apples':5, 'cups':5, 'cookies':1000}
printPicnic(picnicItems, 20, 15)


# In[ ]:




# In[ ]:



