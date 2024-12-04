from geopy import distance
from seoul import relatives,transports
from logTime import defaultLogger

@defaultLogger
def findOneDistance(location1, location2): #Finds a single distance between to relatives
    distance2d = float(distance.distance(location1[-2:], location2[-2:]).km)
    return distance2d

@defaultLogger
def findDistances(): #Creates a list of all possible distances between all relatives
    distances = []
    for r in relatives:
        for r2 in relatives:
            if r != r2:
                distance2d = float(distance.distance(r[-2:], r2[-2:]).km)
                row = [r[0],r2[0],distance2d]
                distances.append(row)
    return distances

@defaultLogger
def createPaths(distances): #Creates paths that inclued 10 different relatices
    distances2 = distances #Creates a duplicate list
    to = []
    paths = []
    pathDistance = 0
    i = 0
    a = 0
    while True:
        if distances[a][0] != distances2[i][1] and distances2[i][1] not in to: #Ensures that only relatives that arent already part of the path are added. NB! Currently not functional!
            pathDistance = distances[a][2] + distances2[i][2]
            to.append(f"{distances2[i][1]}|{str(distances2[i][2])}")

        i += 1
        if i > 10:
            i = 0

        #Shuffles the duplicate list so that the loop doesn't try the same relatives over and over.
        distances2.append(distances2[0])
        distances2.remove(distances2[0])

        #When the list of relatives have all 9 relatives a "path" is created and added to the list of paths
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
def findShortestPath(paths): #Finds the shortest path among a list of paths
    shortestPath = None
    for p in paths:
        if shortestPath == None:
            shortestPath = p
        if p["totalDistance"] < shortestPath["totalDistance"]:
            shortestPath = p
    return shortestPath