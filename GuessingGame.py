# Guessing game
#part 1: In the beginning. . .
import random

print('Hey you, yeah you, what is your name?')
name = input()
attempts = int(6)
print('\n', name + '? That is a good name!', sep='\n', end=' ')
print('How about we play a game? You win, you get to leave, you lose you stay forever.\n\n')
print('What number I am thinking of between 1 and 30? Be careful, you only have ' + str(attempts) + ' guesses!') # made "attempts" variable to print 6 prior to range being declared in part 2
Jackpot = random.randint(1, 30)


#part 2: Win, lose, repeat!
for Numguess in range (1, 7): # allows 6 guesses
    try :
        guess = int(input())
        if guess < Jackpot :
            print('You are too low, try again.')
        elif guess > Jackpot :
            print('You are too high, try again.')
        else:
            break # means they got it correct

    except:
        print('While that may be a number, make it easier on yourself and use the numpad, TRY AGAIN!')

#part 3: The win, the guess, the escape.
if guess == Jackpot :
    print('Wow, you must be a mind reader, kind of freaky if you ask me.')
    print('A deal is a deal, you won our little game, so with that you may leave.')
    print('\n\n\n\n------------------- After credits stats ------------------- ')
    print('You took ' + str(Numguess) + ' guesses, try again to beat your previous score!') # shows how to take the Numguess in the for loop in part 2 and print it
else:
    print('\n\nYou exceeded the amount of ' + str(Numguess) + ' guesses and failed to escape, play again to save yourself.')
    
    
