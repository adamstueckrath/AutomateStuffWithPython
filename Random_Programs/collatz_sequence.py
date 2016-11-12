
# coding: utf-8

# In[ ]:

def collatz(number):
    
    if number%2 == 0:
        print (number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

# Get user input
number = input('Enter a number: ')
while number != 1:
    number = collatz(int(number)) # Call callatz function


# In[ ]:




# In[ ]:



