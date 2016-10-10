import sys


def rotate_around_y_axis(dice):
    """Rotates a dice around its y-axis,
    anti-clockwise seen from origo"""
    return dice[0] + dice[2] + dice[4] + dice[1] + dice[3] + dice[5]

def rotate_around_x_axis(dice):
    """Rotates a dice around its x-axis,
    clockwise seen fro origo"""
    return dice[4] + dice[0] + dice[2] + dice[3] + dice[5] + dice[1]


def bfs_search_dice(goal_dice, queue, visited):
    """Explores if a dice, which is to be sent as [dice] in
    queue-parameter, can be turned to a given goal_dice"""
    if not queue:
        return "FALSE"
    dice = queue.pop(0)
    if dice == goal_dice:
        return "TRUE"
    if dice not in visited:
        queue.append(rotate_around_y_axis(dice))
        queue.append(rotate_around_x_axis(dice))
        visited.append(dice)
    return bfs_search_dice(goal_dice, queue, visited)
    


for dices in sys.stdin:
    if dices != "\n":
        dice1, dice2 = dices[0:6], dices[6:12]
        print(bfs_search_dice(dice2, [dice1], []))
