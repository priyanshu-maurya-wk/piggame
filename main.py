import random

def roll():
    max_roll = 6
    min_roll = 1
    
    dice_roll = random.randint(min_roll, max_roll)
    return dice_roll

while True:
    
    players = input("Enter the number of users (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print(f"There are {players} players")
            break
        else:
            print("Must be between 2-4")
    else:
        print("Enter something valid.🖕")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) <= max_score:
    
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just started!")
        print("Your total score is:", player_score[player_index], "\n")
        score  = 0

        while True:
            should_roll = input("Do you want to roll y/n: ").lower()

            if should_roll != 'y':
                break
            
            value = roll()

            if value == 1:
                score = 0
                print("Your score is 0 because you rolled 1")
                break
            else:
                score += value
                print(f"You rolled a {value}")
                
        player_score[player_index] += score
        print("Your total score is:", player_score[player_index])

max_score = max(player_score)
winning_index = player_score.index(max_score)
print("Player number", winning_index + 1, "is the winner with score of", max_score)
print("Game Over")
print("Thanks for playing!")
print("random stuff")