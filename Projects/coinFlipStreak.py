# Coin Flip Streak Program

# Starting template given:
import random

numberOfStreaks = 0
flips = []
heads = 0
tails = 0
headStreaks = 0
tailStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    for x in range(100):
        result = random.randint(0,1)
        if result == 0:
            heads += 1
            if heads == 6:   # Code that checks for streaks.
                headStreaks += 1
            tails = 0 # Resets tails (1) when heads (0) is cast.
        else:
            tails += 1
            if tails == 6:   # Code that checks for streaks.
                tailStreaks += 1
            heads = 0 # Resets heads (0) when tails (1) is cast.

    numberOfStreaks = headStreaks + tailStreaks

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
