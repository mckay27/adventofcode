with open("input.txt") as f:
    data = f.read().splitlines()


def isVisible(forrest, i, j):
    if (i == 0) or (j == 0) or (i == len(forrest[i]) - 1) or (j == len(forrest) - 1):
        return True

    # Check visibility in -i
    checkI = i
    visible1 = False
    while checkI > 0:
        checkI -= 1
        if forrest[checkI][j] < forrest[i][j]:
            visible1 = True
        else:
            visible1 = False
            break

    visible2 = False
    checkI = i
    while checkI < len(forrest[i]) - 1:
        checkI += 1
        if forrest[checkI][j] < forrest[i][j]:
            visible2 = True
        else:
            visible2 = False
            break

    visible3 = False
    checkJ = j
    while checkJ > 0:
        checkJ -= 1
        if forrest[i][checkJ] < forrest[i][j]:
            visible3 = True
        else:
            visible3 = False
            break

    visible4 = False
    checkJ = j
    while checkJ < len(forrest) - 1:
        checkJ += 1
        if forrest[i][checkJ] < forrest[i][j]:
            visible4 = True
        else:
            visible4 = False
            break

    return visible1 or visible2 or visible3 or visible4


def viewDistance(forrest, i, j):

    # Look -i
    leftScore = 1
    curI = i - 1
    while (curI > 0) and (forrest[curI][j] < forrest[i][j]):
        leftScore += 1
        curI -= 1

    # Look +i
    rightScore = 1
    curI = i + 1
    while (curI < len(forrest[i]) - 1) and (forrest[curI][j] < forrest[i][j]):
        rightScore += 1
        curI += 1

    # Look -j
    upScore = 1
    curJ = j - 1
    while (curJ > 0) and (forrest[i][curJ] < forrest[i][j]):
        upScore += 1
        curJ -= 1

    # Look +j
    downScore = 1
    curJ = j + 1
    while (curJ < len(forrest) - 1) and (forrest[i][curJ] < forrest[i][j]):
        downScore += 1
        curJ += 1

    print(f"left: {leftScore}, right: {rightScore}, up: {upScore}, down: {downScore}")

    return leftScore * rightScore * upScore * downScore


forrest = [[c for c in d] for d in data]

visibleTrees = 0

for i in range(len(forrest)):
    for j in range(len(forrest[i])):
        if isVisible(forrest, i, j):
            visibleTrees += 1

print(f"Visible trees: {visibleTrees}")

scenicScore = 0

for i in range(len(forrest)):
    for j in range(len(forrest[i])):
        localScore = viewDistance(forrest, i, j)
        if localScore > scenicScore:
            scenicScore = localScore

print(f"Scenic score: {scenicScore}")
