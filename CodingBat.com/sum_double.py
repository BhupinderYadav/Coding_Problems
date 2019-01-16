'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    pass

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

def sum_double(a, b):
    try:
        if a == b:
            return (a+b) * 2


        else:
            return a + b
    except:
        print('type should be Integers')

if __name__ == '__main__':
    x = sum_double(1, 2)
    print(x)
    x = sum_double(3, 2)
    print(x)
    x = sum_double(2, 2)
    print(x)
    x = sum_double('a', 2)
    print(x)
