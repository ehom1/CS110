import random

random_num = int(random.randint(1, 10))

guess = int(input("Guess the random number: "))

if random_num == guess:
    print("correct!")
elif guess < random_num:
    print("too low")
    guess2 = int(input("Next guess: "))
    if random_num == guess2:
        print("correct!")
    elif random_num < guess2:
        print("too high")
        guess3 = int(input("Final guess: "))
        if random_num == guess3:
            print("correct!")
        else:
            print("wrong. the number was", random_num)
    elif random_num > guess2:
        print("too low")
        guess3 = int(input("Final guess: "))
        if random_num == guess3:
            print("correct!")
        else:
            print("wrong. the number was", random_num)
elif guess > random_num:
    print("too high")
    guess2 = int(input("Next guess: "))
    if random_num == guess2:
        print("correct!")
    elif random_num < guess2:
        print("too high")
        guess3 = int(input("Final guess: "))
        if random_num == guess3:
            print("correct!")
        else:
            print("wrong. the number was", random_num)
    elif random_num > guess2:
        print("too low")
        guess3 = int(input("Final guess: "))
        if random_num == guess3:
            print("correct!")
        else:
            print("wrong. the number was", random_num)