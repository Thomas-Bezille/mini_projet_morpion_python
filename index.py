map = [
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
]

player = "Joueur 1"

def draw() -> None:
    '''Displays the nine cells of the game in the format: 3 rows and 3 columns'''
    for i in range(3):
        for j in range(3):
            print(map[i][j], end="")
        print()

def check_win() -> bool:
    '''Check if a player has won the game by checking the rows, columns and diagonals'''
    for i in range(3):
       if map[i][0] == map[i][1] == map[i][2] != " . ": # Check rows
           return True
    for i in range(3):
       if map[0][i] == map[1][i] == map[2][i] != " . ": # Check columns
           return True
    if map[0][0] == map[1][1] == map[2][2] != " . " or map[0][2] == map[1][1] == map[2][0] != " . ": # Check diagonals
        return True
    return False

def check_draw() -> bool:
    '''Check if there are still empty cells in the matrix'''
    for i in range(3):
        for j in range(3):
            if map[i][j] == " . ":
                return False
    return True

draw()

while True:
    choice = int(input(f"{player} [1-9] ? > "))
    row = (choice - 1) // 3
    cullumn = (choice - 1) % 3
    if map[row][cullumn] == " . ":
        map[row][cullumn] = " X " if player == "Joueur 1" else " O "
    draw()
    if check_win():
        print(f"{player} a gagné !")
        break
    if check_draw():
        print("Match nul !")
        break
    player = "Joueur 2" if player == "Joueur 1" else "Joueur 1"