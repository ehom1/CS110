import random

number = int(random.randint(1, 1000))
print (number)

number_guesses = 0

while True:
    guess = int(input("Guess the random number between 1 and 1000: "))
    number_guesses += 1
    
    if guess == number:
        print("Correct! You guessed the random number in", number_guesses, "tries.")
        break
    elif guess < number:
        print("Try a higher number.")
    elif guess > number:
        print("Try a lower number.")