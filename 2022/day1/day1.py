def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    elves = list()
    elves.append(list())
    curInd = 0

    for cal in data:
        if cal != "":
            elves[curInd].append(int(cal))
        else:
            curInd += 1
            elves.append(list())

    elfTotals = list()

    for elf in elves:
        localMax = 0
        for cal in elf:
            localMax += cal

        elfTotals.append(localMax)

    elfTotals.sort(reverse=True)

    print(
        f"Max calories carried by top three elves: {elfTotals[0] + elfTotals[1] + elfTotals[2]}"
    )


if __name__ == "__main__":
    main()
