pos1 = 6
pos2 = 2
score1 = 0
score2 = 0
p1_move = True

# Part 1
"""dice = 1
dice_count = 0
while score1 < 1000 and score2 < 1000:
    step = 0
    for i in range(3):
        step += dice
        dice_count += 1
        dice += 1
        if dice == 101: dice = 1
    
    if p1_move:
        pos1 += step
        pos1 = pos1 % 10 if pos1 % 10 != 0 else 10
        score1 += pos1
        p1_move = not p1_move
    else: 
        pos2 += step
        pos2 = pos2 % 10 if pos2 % 10 != 0 else 10
        score2 += pos2
        p1_move = not p1_move
print(dice_count * score2)"""

#wins = [0, 0]

p = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

def turn(score1, score2, pos1, pos2, p1_move):
    if score1 >= 21 or score2 >= 21: return int(score1 >= 21), int(score2 >= 21)

    wins_local = [0,0]

    for d in p:
        if p1_move:
            pos1 += d
            pos1 = pos1 % 10 if pos1 != 10 else 10
            winners = turn(score1 + pos1, score2, pos1, pos2, not p1_move)
            wins_local[0] += winners[0] * p[d]
            wins_local[1] += winners[1] * p[d]
        else:
            pos2 += d
            pos2 = pos2 % 10 if pos2 != 10 else 10
            winners = turn(score1, score2 + pos2, pos1, pos2, not p1_move)
            wins_local[0] += winners[0] * p[d]
            wins_local[1] += winners[1] * p[d]
    
    return wins_local

wins = turn(0, 0, pos1, pos2, True)
print(wins)
print(max(wins))

