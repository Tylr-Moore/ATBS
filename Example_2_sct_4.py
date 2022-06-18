print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
          print('That is a lot of cats.')
    elif int(numCats) >= 0 and int(numCats)< 4: #Q&A hint with elif, but this shows me how to do operators.
        print('That is not that many cats.')
    elif int(numCats) < 0:
        print('You cant have less than 0 cats.')
except ValueError:
    print('You did not enter a number.')
