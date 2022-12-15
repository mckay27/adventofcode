with open("input.txt") as f:
    data = f.read().splitlines()

pairs = list()
for d in data:
    pairs.append(d.split(","))

count = 0
for pair in pairs:
    top = pair[0].split("-")
    bot = pair[1].split("-")
    topLeft = int(top[0])
    topRight = int(top[1])
    botLeft = int(bot[0])
    botRight = int(bot[1])

    print(f"tL: {topLeft}, tR: {topRight}, bL: {botLeft}, bR: {botRight}")

    if (
        ((topLeft <= botRight) and (topLeft >= botLeft))
        or ((topRight <= botRight) and (topRight >= botLeft))
        or ((botLeft <= topRight) and (botLeft >= topLeft))
        and ((botRight <= topRight) and (botRight >= topLeft))
    ):
        print(f"pair: {pair} one overlaps the other")
        count += 1

print(f"Number of pairs: {count}")
