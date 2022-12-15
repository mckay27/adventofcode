with open("input.txt") as f:
    data = f.read().splitlines()


class Node:
    directories = list()

    def __init__(self, name=None, parent=None, size=None):
        self.parent = parent
        self.size = size
        self.name = name
        self.children = list()

    def getChild(self, name):
        for c in self.children:
            if name == c.name:
                return c

    def __str__(self) -> str:
        return f"<Node {self.name}:{self.size}>"

    def printTree(self):
        output = str(self)
        if len(self.children) > 0:
            for c in self.children:
                output += "\n" + c.printTree()
        return "\t".join(output.splitlines(True))

    def calcSizes(self):
        if self.size is not None:
            return self.size

        for c in self.children:
            c.calcSizes()

        self.size = sum(c.size for c in self.children)

        return self.size


tree = Node()
tree.children.append(Node(name="/"))

currentNode = tree
for cmd in data:
    cmd_s = cmd.split()

    # If it's a command
    if cmd_s[0] == "$":
        # If it's a cd
        if cmd_s[1] == "cd":
            if cmd_s[2] == "..":
                # print(f"Changing up to {currentNode.parent}")
                currentNode = currentNode.parent
            else:
                # print(f"Changing into {cmd_s[2]}")
                currentNode = currentNode.getChild(cmd_s[2])

        # If it's an ls
        elif cmd_s[1] == "ls":
            pass

    # If it's a folder
    elif cmd_s[0] == "dir":
        # print(f"Adding {cmd_s[1]} to {currentNode}")
        newNode = Node(name=cmd_s[1], parent=currentNode)
        currentNode.children.append(newNode)
        Node.directories.append(newNode)

    # it's a file
    else:
        # print(f"Adding {cmd_s[1]} to {currentNode}")
        currentNode.children.append(
            Node(name=cmd_s[1], size=int(cmd_s[0]), parent=currentNode)
        )

tree.calcSizes()
print("Print tree")
print(tree.printTree())
directorySum = sum(n.size for n in Node.directories if n.size < 100000)
print(f"\nSum Tree: {directorySum}")

usedSpace = tree.size
freeSpace = 70000000 - usedSpace
spaceToFree = 30000000 - freeSpace

directorySizes = [n.size for n in Node.directories if n.size > spaceToFree]
directorySizes.sort()
print(f"\nSize of directory to delete {directorySizes}")
