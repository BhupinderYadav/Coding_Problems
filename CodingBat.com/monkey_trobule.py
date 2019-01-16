'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    pass

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''

def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        print ('you are in trouble, run')
        return True

    elif a_smile != True and b_smile != True:
        print ('you are in trouble, run')
        return True

    else:
        print ('it's ok, you will survive')
        return False

if __name__ == '__main__':
    monkey_trouble(True, True)
    monkey_trouble(False, False)
    monkey_trouble(True, False)
