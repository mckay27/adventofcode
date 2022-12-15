with open("input.txt") as f:
    data = f.read()

marker = [
    data[0],
    data[1],
    data[2],
    data[3],
    data[4],
    data[5],
    data[6],
    data[7],
    data[8],
    data[9],
    data[10],
    data[11],
    data[12],
    data[13],
]

for i in range(4, len(data)):
    validMarker = True
    for c in marker:
        if marker.count(c) > 1:
            validMarker = False
            break

    if validMarker:
        print(f"Marker found at: {i}")
        break

    marker.pop(0)
    marker.append(data[i])
