target = 7
guess = int(input("Try to guess ze numba from range 0-20: "))

while guess != 7:
    print("Nope ", guess, " isn't ze numba you are looking for! Try again.")
    attempt = 0
    attempt = attempt + 1
    print("This was attempt no.", attempt, ".")
    guess = int(input("Try to guess ze numba from range 0-20: "))
print("Good job!", target, " is the correct numba! You got it in", attempt, "tries!")
