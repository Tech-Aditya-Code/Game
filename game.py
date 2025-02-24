import random
import time


message = "Guess a number between 1 to 10"

for char in message:
    print(char, end="", flush=True)
    # extend execution with 0.2s
    time.sleep(0.2)

print("\n")

def game():
    n = int(input("Enter a number: "))

    r = random.randint(1,10)
    print("The number is: ",r)

    
    if (n == r):
        print("you guess the right number!")
    else:
        print("you guess the wrong number!")
    game()
game()

