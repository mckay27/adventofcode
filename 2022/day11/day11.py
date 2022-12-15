with open("input.txt") as f:
    data = f.read().splitlines()

NUM_ROUNDS = 10000

class Monkey:
    def __init__(self, id, items, op, test, trueResult, falseResult):
        self.id = id
        self.items = items
        self.op = op
        self.test = test
        self.trueResult = trueResult
        self.falseResult = falseResult
        self.inspected = 0

monkeys = list()

# Parse input
for i in range(0, len(data) + 1, 7):

    # Get items
    itemList = [int(x) for x in data[i+1][18:].split(", ")]

    # Get operation
    op = eval("lambda old: old " + data[i+2][23] + " " + data[i+2][25:])

    # Get test
    test = int(data[i+3][21:])

    # Get monkeys
    trueMonkey = int(data[i+4][29:])
    falseMonkey = int(data[i+5][30:])

    monkeys.append(Monkey(int(i/7), itemList, op, test, trueMonkey, falseMonkey))

commonD = monkeys[0].test
for i in range(1,len(monkeys)):
    commonD *= monkeys[i].test


for r in range(1, NUM_ROUNDS+1):
    print(f"ROUND {r}")
    for monkey in monkeys:
        # print(f"\tMonkey {monkey.id}")
        for i in range(len(monkey.items)):
            monkey.inspected += 1
            # print(f"\t\tMonkey inspects item with worry {monkey.items[0]}")
            # Increase worry
            monkey.items[0] = monkey.op(monkey.items[0])
            # print(f"\t\t\tWorry level increased to: {monkey.items[0]}")

            # Decrease worry
            monkey.items[0] = int(monkey.items[0] % commonD)
            # print(f"\t\t\tWorry decreased to {monkey.items[0]}")

            # Test item
            if (monkey.items[0] % monkey.test) == 0:
                # print(f"\t\t\tWorry is divisible by {monkey.test}")
                monkeyThrow = monkey.trueResult
            else:
                # print(f"\t\t\tWorry is not divisible by {monkey.test}")
                monkeyThrow = monkey.falseResult

            # print(f"\t\t\tMonkey threw item to monkey {monkeyThrow}")
            monkeys[monkeyThrow].items.append(monkey.items[0])
            monkey.items.pop(0)

    # print(f"\nCurrent monkey holdings after round {r}")
    # for monkey in monkeys:
    #     print(f"Monkey {monkey.id}: {monkey.items}")
    # print("")

print(f"Number of times monkeys inspected items")
inspected = [x.inspected for x in monkeys]
for monkey in monkeys:
    print(f"Monkey {monkey.id}: {monkey.inspected}")

inspected.sort(reverse=True)
print(f"Monkey activity: {inspected[0] * inspected[1]}")