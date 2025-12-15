import random

score = 0

while True:
    user = input("Roll the dice y/n? ")

    if user == 'y':
        roll = random.randint(1,6)
        score = score + roll
        print(f"Dice rolled: {roll}")
        
        if roll == 1:
            score = score + roll
            break
        else:
            continue
        
    elif user == 'n':
        print(score)
        break
    else:
        print("Enter something valid")

print(f"Final score: {score}")
print("Game Over")