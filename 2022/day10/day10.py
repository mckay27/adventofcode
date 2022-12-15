with open("input.txt") as f:
    data = f.read().splitlines()

INSTRUCTIONS = ["noop", "addx"]

curCycle = 0

xReg = 1

signalStrength = 0

crt = ["." for x in range(6 * 40)]

def checkSprite(spritePos, cycleNum):
    if (cycleNum-1)%40 in [spritePos - 1, spritePos, spritePos + 1]:
        return "#"
    else:
        return "."

for d in data:
    inst = d.split()

    curCycle += 1

    # ADDX
    if inst[0] == INSTRUCTIONS[1]:
        # If it's a multiple of 20 cycle
        if (curCycle - 20) % 40 == 0:
            signalStrength += curCycle * xReg

        crt[curCycle-1] = checkSprite(xReg, curCycle)

        curCycle += 1
        
        crt[curCycle-1] = checkSprite(xReg, curCycle)
        if (curCycle - 20) % 40 == 0:
            signalStrength += curCycle * xReg

        # Update x reg
        xReg += int(inst[1])

    else:
        if (curCycle - 20) % 40 == 0:
            signalStrength += curCycle * xReg

        crt[curCycle-1] = checkSprite(xReg, curCycle)

    



print(f"Signal Strength: {signalStrength}")

print(crt)

print("\n\n------------------CRT-------------------")
for y in range (6):
    for x in range(40):
        print(f"{crt[x+(40*y)]}", end="")

    print("")