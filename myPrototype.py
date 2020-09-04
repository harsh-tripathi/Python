number = 30
guess = 1
while guess <= 9:
    num = int(input("Guess a number : "))
    if 9-guess == 0:
        print("You ran out of guesses.")
        print("Man you suck at this game.")
        break
    elif num < number:
        print("Guess a bigger number.")
        print("You have",9-guess,"guesses left.")
        guess = guess+1
        continue
    elif num > number:
        print("Guess a smaller number.")
        print("You have",9-guess,"guesses left.")
        guess = guess+1
        continue
    else:
        print("Well Done, You guessed it correct!!")
        print("Game Over!")
        print("You answered correctly after",guess,"guesses.")
        break