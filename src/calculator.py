from geopy import distance
from seoul import relatives,transports
from logTime import defaultLogger

@defaultLogger
def findOneDistance(location1, location2):
    distance2d = float(distance.distance(location1[-2:], location2[-2:]).km)
    return distance2d

@defaultLogger
def findDistances():
    distances = []
    for r in relatives:
        for r2 in relatives:
            if r != r2:
                distance2d = float(distance.distance(r[-2:], r2[-2:]).km)
                row = [r[0],r2[0],distance2d]
                distances.append(row)
    return distances

@defaultLogger
def createPaths(distances):
    distances2 = distances
    to = []
    paths = []
    pathDistance = 0
    i = 0
    a = 0
    while True:
        """ if distances[a][0] != distances2[i][1] and distances2[i][1] not in to:
            pathDistance = distances[a][2] + distances2[i][2]
            to.append(f"{distances2[i][1]}|{str(distances2[i][2])}") """

        if distances[a][0] != distances[i][0] and distances[i][1] not in to:
            pathDistance += distances[a][2] + distances[i][2]
            to.append(f"{distances[i][1]}|{str(distances[i][2])}")

        i += 1
        if i > 10:
            i = 0

        #distances2.append(distances2[0])
        #distances2.remove(distances2[0])
        if len(to) == 9:
            path = {"From": distances[a][0], "To": to, "totalDistance": pathDistance}
            paths.append(path)
            to = []
            pathDistance = 0.0

            a += 1
            if a > 10:
                a = 0

        if len(paths) == 90:
            break

    return paths



@defaultLogger
def findShortestPath(paths):
    shortestPath = None
    for p in paths:
        if shortestPath == None:
            shortestPath = p
        if p["totalDistance"] < shortestPath["totalDistance"]:
            shortestPath = p
    return shortestPath

def findTransports():
    #.rpartition("|")[2]

    return

#print(findShortestPath(createPaths(findDistances())))
paths = createPaths(findDistances())
for p in paths:
    print(p)

