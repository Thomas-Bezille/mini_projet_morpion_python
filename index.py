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

draw()

while True:
    choice = int(input(f"{player} [1-9] ? > "))
    row = (choice - 1) // 3
    cullumn = (choice - 1) % 3
    if map[row][cullumn] == " . ":
        map[row][cullumn] = " X " if player == "Joueur 1" else " O "
    draw()
    player = "Joueur 2" if player == "Joueur 1" else "Joueur 1"