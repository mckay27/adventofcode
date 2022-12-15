with open("input.txt") as f:
    data = f.read().splitlines()


curCrates = list()

for d in data:
    if d == "":
        break
    curCrates.append(d)


# Get crate labels
labels = curCrates[-1].split()

crates = list()

for i in labels:
    crates.append(list())
    for row in curCrates[-2::-1]:
        crate = row[((int(i) - 1) * 4) + 1 : ((int(i) - 1) * 4) + 2]
        if crate != " ":
            crates[-1].append(crate)


moves = data[10:]

for move in moves:
    rawMove = move.split()

    qty = int(rawMove[1])
    src = int(rawMove[3])
    dst = int(rawMove[5])

    movingStack = crates[src - 1][-qty:]
    print(
        f"Move: {move}, src: {crates[src-1]}, dst: {crates[dst-1]}, stack: {movingStack}"
    )
    crates[src - 1] = crates[src - 1][:-qty]
    crates[dst - 1].extend(movingStack)

    # for i in range(qty):
    #     movingCrate = crates[src - 1].pop(-1)
    #     crates[dst - 1].append(movingCrate)

# Get top of stacks
print(crates)
output = ""
for stack in crates:
    output += str(stack[-1])

print("Tops of the stacks: " + output)
