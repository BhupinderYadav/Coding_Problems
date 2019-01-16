'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
we will sleep if vaccation and weekends and we will be working if its weekday and no vaccation.

def sleep_in(weekday, vacation):
    pass

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in(weekday, vacation):
    if weekday != True and vacation != True:
        print(True)
        print('go sleep, its a weekend')
    elif weekday == True and vacation == True :
        print(True)
        print('go and sleep, its a holiday')

    else:
        print(False)
        print('go work, nither holiday nor weekend')

if __name__ == '__main__':
    sleep_in(False, False)
    sleep_in(True, False)
    sleep_in(False, True)
