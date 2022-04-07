import random
map = [
    [12, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 24]
]

def get_start_pos():
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == 12:
                return y, x

startY, startX = get_start_pos()

rowX = len(map[0])

colY = len(map)

def get_next_free_pos(current_posY, current_posX):
    possible_moves = []
    
    if current_posX + 1 < colY and map[current_posY][current_posX + 1] in [1, 24]:
        print("can go right")
        possible_moves.append((current_posY, current_posX + 1))
    
    if current_posX - 1 >= 0 and map[current_posY][current_posX - 1] in [1, 24]:
        print("can go left")
        possible_moves.append((current_posY, current_posX - 1))
    
    if current_posY + 1 < colY and map[current_posY + 1][current_posX] in [1, 24]:
        print("can go down")
        possible_moves.append((current_posY + 1, current_posX))
    
    if current_posY - 1 >= 0 and map[current_posY - 1][current_posX] in [1, 24]:
        print("can go up")
        possible_moves.append((current_posY - 1, current_posX))
    
    if map[current_posY][current_posX] == 24:
        print("FINISH")
        return False
    
    random_move = random.choice(possible_moves)
    
    print(random_move)
    
    return random_move

next_free_pos = get_next_free_pos(startY, startX)

print("next free pos", next_free_pos)

while next_free_pos:
    next_free_pos = get_next_free_pos(next_free_pos[0], next_free_pos[1])
    print("next free pos", next_free_pos)