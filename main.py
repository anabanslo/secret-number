secret = 10

guess = int(input("Guess the secret number between 1 and 30: "))

if guess == secret:
    print("Congratz, that's my number!")
else:
    print("Eee wrooong, not " + str(guess) + "! Guess again!")