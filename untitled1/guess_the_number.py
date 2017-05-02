import random

NUMBER_OF_GUESSES = 3
RANGE = 10

while True:
    # generate the random number
    random_number = random.randint(0, RANGE)

    # give the user a certain amount of guesses
    for i in range(NUMBER_OF_GUESSES):
        guess = int(raw_input('guess the number: '))
        if guess == random_number:
            print 'well done'
            continue
        elif guess > random_number:
            print "too high"
        else:
            print "too low"

    print "sorry, you've had all your guesses, let's try a new number"