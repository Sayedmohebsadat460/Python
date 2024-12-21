#  Guess number
import random
run = random.randint(1,10)
print(run)
guess = int(input("Guess number: "))
if run == guess :
    print("You Win")
else :
    print("Try again")