input_prompt = int(input("Enter a number: "))

### NOTE, I changed the input argument of each function from inputnum to x
### Sum of odd numbers implementations of square root

'''
perfect squares are the sum of odd numbers
1  = 1
4  = 1+3
9  = 1+3+5
16 = 1+3+5+7
25 = 1+3+5+7+0

sqrt(16) = 1+3+5+7 <- we added 4 numbers to get to 16 -> sqrt(16) = 4
sqrt(25) = 1+3+5+7+9 <- we added 5 numbers -> sqrt(25) = 5
sqrt(21) = 1+3+5+7+9... 25 is over 21
         = 1+3+5+7+5 => added 4 numbers together and remainder is 5/9 => sqrt(21) ~= 4+5/9
sqrt(18) = 1+3+5+7+9... 25 is over 18
         = 1+3+5+7+2 => 18 is over 16 by 2. so remainder is 2/9 => sqrt(18) ~= 4+2/9

         implement using for/while?
'''

''' generating odd numbers = 2*index+1
index = 0; odd = 1;
index = 1 ; odd = 3;
index = 2; odd = 5;
'''

def sqrt1(x):
    print('using conditional-while')
    acc = 0
    index = 0
    while (acc < x):
        odd = 2 * index + 1
        acc += odd
        index += 1
    remainder = x - (acc - odd) # for 18, 18-(25-9) = 18-16 = 2
    return (index-1 + remainder/odd)

def sqrt2(x):
    print('using while with break')
    acc = 0
    index = 0
    while True:
        odd = 2 * index + 1
        acc += odd
        if (acc > x):
            break
        index += 1 # index = index + 1
    remainder = x - (acc - odd) # for 18, 18-(25-9) = 18-16 = 2
    return (index + remainder/odd)

def sqrt3(x):
    print('using for loop')
    acc = 0
    for index in range(1000):
        odd = 2 * index + 1
        acc += odd
        #print(index, odd, acc)
        if (acc > x):
            break
    remainder = x - (acc - odd) # for 18, 18-(25-9) = 18-16 = 2
    return (index + remainder/odd) # for 18, 4+2/9'''

#print(sqrt3(input_prompt))

### Newton's algorithm for square root - see case study for chapter 3

# guess = ( guess + x/guess )/2
TOLERANCE = .00001 # how close do we want to get to the answer
GUESS = 20 # starting guess

def sqrt4(x, guess = GUESS, tolerance = TOLERANCE):
    print('using while true loop with break')
    while True:
        previous_guess = guess
        guess = ( guess + x/guess )/2
        difference = abs(previous_guess-guess)
        if (difference < tolerance):
            break
    return guess

def sqrt5(x, guess = 20, tolerance = .0005):
    if (x < 0):
        return 'imaginary'
    print('using conditional while loop')
    difference = guess
    while (difference > tolerance):
        previous_guess = guess
        guess = ( guess + x/guess )/2
        difference = abs(previous_guess-guess)
    return guess

sqrt_result = sqrt5( input_prompt+5 )
print( sqrt_result )

## ======

def washing_clothes(dirty_clothes, laundry_detergent='Tide',
                    fabric_softener=None):
     print('gets quarters')
     print('goes to washers')
     print('load washer')
     print(f'put in {laundry_detergent} and {fabric_softener}')
     print('...')
     return 'wet clothes'

def drying_clothes(wet_clothes):
    ....

def doing_laundry(dirty_clothes):
    wet_clothes = washing_clothes(dirty_clothes):
    clean_clothes = drying_clothes(wet_clothes)