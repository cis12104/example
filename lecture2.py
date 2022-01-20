# lecture 2

''' the argument to the input function is a string
 in this example we provide a string literal, but it can be
 an expression that evaluates to a string'''
# we store the result of the right side into the variable on the left
first_str = input('Enter the first number: ')
first_int = int(first_str)
second = float(input('Enter the second number: '))
# notice we are escaping the single quote in you're and adding a new line and tab
print("You\'re summing", first_int, "and", second, "\n\tto get", first_int+second)
print("You\'re summing", first_str, "and", second, "\n\tto get", first_int+second)
print(f'You\'re summing {first_int} and {second} \n\tto get {first_int + second}')
#print("You\'re summing", first_int, "and", second, "\n\tto get", first_str+second) # this would be a TypeError

print('\n\n')

repeat = input('How many times would you like to say \'Python\'? ')
#repeat = 10  # uncomment this line to set the variable in your code and not use user input
print(int(repeat) * 'Python')

profit = 1000 # profit is an int, we need to cast it to a string to add a dollar sign
print('The profit is:\t$' + str(profit))

# comments can be defined using # (single line) or '''
'''
Commenting
multiple
lines
'''