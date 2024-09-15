map = [
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
    [" . ", " . ", " . "],
]

def draw() -> None:
    '''Displays the nine cells of the game in the format: 3 rows and 3 columns'''
    for i in range(3):
        for j in range(3):
            print(map[i][j], end="")
        print()

