# Imports
import os

# Variables
rows, columns = 3, 3
player_turn = [1, "X"]
played = []
position = ["Top Left", "Top Centre", "Top Right", "Left Middle", "Middle Centre", "Middle Right", "Bottom Left", "Bottom Centre", "Bottom Right"]
grid = [[[False, " ", row + (column * 3) + 1] for row in range(rows)] for column in range(columns)]
game_over = False

# Clear Screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print Board
def board():
    global grid
    print(f"""
            |         |         
        {grid[0][0][1]}   |    {grid[0][1][1]}    |    {grid[0][2][1]}           
            |         |         
    -----------------------------
            |         |         
        {grid[1][0][1]}   |    {grid[1][1][1]}    |    {grid[1][2][1]}           
            |         |         
    -----------------------------
            |         |         
        {grid[2][0][1]}   |    {grid[2][1][1]}    |    {grid[2][2][1]}           
            |         |         
    """)

# Turn
def turn():
    global position, grid, game_over
    swap_player()
    for i in range(rows):
        for j in range(columns):
            if grid[i][j][0] == False:
                place = grid[i][j][2]
                print(f"Press {place} to place your {player_turn[1]} in the {position[place - 1]}.")
    user_input = validate()
    for i in range(rows):
        for j in range(columns):
            if grid[i][j][2] == user_input:
                grid[i][j][1] = player_turn[1]
                grid[i][j][0] = True
                played.append(user_input)
    clear()            
    board()
    game_over = win_check()

def swap_player():
    global player_turn
    if len(played) % 2 == 0:
        player_turn = [1, "X"]
    else:
        player_turn = [2, "O"]

# Error Handling
def validate():
    global played
    try:
        choice = int(input(f"\nPlayer {player_turn[0]}, where would you like to place your {player_turn[1]}? >>> "))
        if choice not in played and choice in range(1, 10):
            return choice
        else:
            print("That is not a valid option, please try again.")
            return validate()
    except:
        print("That is not a valid option, please try again.")
        return validate()

# Win condition check
def win_check():
    global played, grid, player_turn56
    if grid[0][0][1] == grid[0][1][1] and grid[0][0][1] == grid[0][2][1] and grid[0][0][1] != " " or grid[1][0][1] == grid[1][1][1] and grid[1][0][1] == grid[1][2][1] and grid[1][0][1] != " " or grid[2][0][1] == grid[2][1][1] and grid[2][0][1] == grid[2][2][1] and grid[2][0][1] != " " or grid[0][0][1] == grid[1][0][1] and grid[0][0][1] == grid[2][0][1] and grid[0][0][1] != " " or grid[0][1][1] == grid[1][1][1] and grid[0][1][1] == grid[2][1][1] and grid[0][1][1] != " " or grid[0][2][1] == grid[1][2][1] and grid[0][2][1] == grid[2][2][1] and grid[0][2][1] != " " or grid[0][0][1] == grid[1][1][1] and grid[0][0][1] == grid[2][2][1] and grid[0][0][1] != " " or grid[0][2][1] == grid[1][1][1] and grid[0][2][1] == grid[2][0][1] and grid[0][2][1] != " ":
        print(f"Congratulations to player {player_turn[0]} on their victory!")
        return True
    elif len(played) >= 9:
        print("The game is a draw!")
    else:
        return False

# Main
def main():
    global game_over, player_turn
    clear()
    print("Welcome to Neil's Noughts and Crosses")
    board()
    while game_over == False:
        turn()

main()