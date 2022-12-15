with open("testinput.txt") as f:
    data = f.read().splitlines()


class Knot:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
        self.xLast = initX
        self.yLast = initY

    def newPos(self, newX, newY):
        self.xLast = self.x
        self.yLast = self.y

        self.x = newX
        self.y = newY

    def move(self, xOffset, yOffset):
        self.xLast = self.x
        self.yLast = self.y

        self.x += xOffset
        self.y += yOffset


BOARD_SIZE = 40

NUM_KNOTS = 10

STARTX = int(BOARD_SIZE / 2)
STARTY = int(BOARD_SIZE / 2)

visitedT = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
# visitedH = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

visitedT[STARTX][STARTY] = 1
# visitedH[STARTX][STARTY] = 1

rope = [Knot(STARTX, STARTY) for x in range(NUM_KNOTS)]


for d in data:
    move = d.split()
    print(f"Move: {d}")

    for i in range(int(move[1])):

        # Perform move
        if move[0] == "R":
            rope[0].move(1, 0)
        elif move[0] == "L":
            rope[0].move(-1, 0)
        elif move[0] == "U":
            rope[0].move(0, 1)
        elif move[0] == "D":
            rope[0].move(0, -1)

        for i in range(1, len(rope)):
            if rope[i].x not in range(rope[i - 1].x - 1, rope[i - 1].x + 2) or rope[
                i
            ].y not in range(rope[i - 1].y - 1, rope[i - 1].y + 2):
                # If leading knot is moved diagonally
                if (
                    abs(rope[i - 1].x - rope[i - 1].xLast) == 1
                    and abs(rope[i - 1].y - rope[i - 1].yLast) == 1
                ):
                    # Move current knot diagonally in same direction
                    rope[i].move(
                        rope[i - 1].x - rope[i - 1].xLast,
                        rope[i - 1].y - rope[i - 1].yLast,
                    )

                # Moved right
                elif (rope[i - 1].x - rope[i - 1].xLast) == 1:
                    rope[i].newPos(rope[i - 1].x - 1, rope[i - 1].y)

                # Moved left
                elif (rope[i - 1].x - rope[i - 1].xLast) == -1:
                    rope[i].newPos(rope[i - 1].x + 1, rope[i - 1].y)

                # Moved up
                elif (rope[i - 1].y - rope[i - 1].yLast) == 1:
                    rope[i].newPos(rope[i - 1].x, rope[i - 1].y - 1)

                # Moved down
                elif (rope[i - 1].y - rope[i - 1].yLast) == -1:
                    rope[i].newPos(rope[i - 1].x, rope[i - 1].y + 1)

        # Add tail position
        visitedT[rope[9].x][rope[9].y] = 1

        # Add Head position
        # visitedH[curHX][curHY] = 1

        print("\t", end="")
        for i in range(len(rope)):
            print(f"{i}:[{rope[i].x}][{rope[i].y}] ", end="")
        print("")


# Count positions visisted
visitedCount = 0
for x in range(BOARD_SIZE):
    for y in range(BOARD_SIZE):
        if visitedT[x][y] == 1:
            visitedCount += 1

print("\nVisited Tail array")
for y in range(BOARD_SIZE - 1, 0 - 1, -1):
    for x in range(BOARD_SIZE):
        print(f"[{visitedT[x][y]} ", end="")

    print("")

print(f"\n\nTail visitied {visitedCount} spots")
