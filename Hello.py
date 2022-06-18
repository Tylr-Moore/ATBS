# This program says hello and asks for my name

print('Hello World!')

print('What is your name? (Input F/L name)') # asks for their name
myName = input()
print('Awesome, it is nice to meet you ' + myName)
print('Interesting fact, did you know your name is ')
print(len(myName) - 1) # The - 1 accounts for the space
print('characters long? How neat!')


print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


