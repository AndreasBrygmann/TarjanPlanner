#Relative, Street Name, District (Gu), Latitude, Longitude
relatives = [
    ["Relative_1", "Gangnam-daero", "Gangnam-gu", 37.4979, 127.0276],
    ["Relative_2", "Yangjae-daero", "Seocho-gu", 37.4833, 127.0322],
    ["Relative_3", "Sinsa-daero", "Gangnam-gu", 37.5172, 127.0286],
    ["Relative_4", "Apgujeong-ro", "Gangnam-gu", 37.5219, 127.0411],
    ["Relative_5", "Hannam-daero", "Yongsan-gu", 37.5340, 127.0026],
    ["Relative_6", "Seongsu-daero", "Seongdong-gu", 37.5443, 127.0557],
    ["Relative_7", "Cheongdam-ro", "Gangnam-gu", 37.5172, 127.0391],
    ["Relative_8", "Bukhan-ro", "Jongno-gu", 37.5800, 126.9844],
    ["Relative_9", "Samseong-ro", "Gangnam-gu", 37.5110, 127.0590],
    ["Relative_10", "Jamsil-ro", "Songpa-gu", 37.5133, 127.1028]
]
#Mode of Transport, Speed_kmh, Cost_per_km, Transfer_Time_min
transports = [
    ["Bus", 40, 2, 5],
    ["Train", 80, 5, 2],
    ["Bicycle", 15, 0, 1],
    ["Walking", 5, 0, 0]
]

from geopy import distance
#distance_2d = distance.distance(relatives[0][-2:], relatives[1][-2:]).m
#print(distance_2d)

""" distances = []
paths = []
i = 0
for r in relatives:
    for r2 in relatives:
        if r != r2:
            distance2d = float(distance.distance(r[-2:], r2[-2:]).m)
            #explainer = str(distance2d) + f" meters to {r2[0]}"
            #row = {"Index": i, "From": r[0], "To": r2[0], "Distance": distance2d}
            row = [r[0],r2[0],distance2d]
            #oneRelative.append(row)
            distances.append(row)
            i += 1
paths = []
distances2 = distances
i = 0 """
""" for d in range(len(distances)):
    for relative in range(len(distances[d])):
        to = []
        pathDistance = 0.0
        #for relative2 in range(9):
        while True:
            '''
            pathDistance = d["Distance"] + distances2[relative2]["Distance"]
            to.append(distances2[relative2]["To"])
            distances2.append(distances2.pop(distances2[0]["Index"])) 
            '''
            if distances[d] != distances2[i]:
                pathDistance = distances[d][2] + distances2[i][2]
                to.append(distances2[i][1])
                #distances2.append(distances2.pop(distances2.index(0)))
            i += 1
            if i > 10:
                i = 0
            distances2.append(distances2[0])
            distances2.remove(distances2[0])
            if len(to) == 9:
                path = {"From": distances[d][0], "To": to, "totalDistance": pathDistance}
                paths.append(path)
                to = []
                pathDistance = 0.0
            if len(paths) == 90:
                break """

    #path = {"From": d["From"], "To": to, "totalDistance": pathDistance}
""" a = 0
to = []
while True:
    if distances[a][0] != distances2[i][1] and distances2[i][1] not in to:
        pathDistance = distances[a][2] + distances2[i][2]
        to.append(distances2[i][1])

    i += 1
    if i > 10:
        i = 0

    distances2.append(distances2[0])
    distances2.remove(distances2[0])
    if len(to) == 9:
        path = {"From": distances[a][0], "To": to, "totalDistance": pathDistance}
        paths.append(path)
        to = []
        pathDistance = 0.0

        a += 1
        if a > 10:
            a = 0

    if len(paths) == 90:
        break """

""" shortestPath = None
for p in paths:
    if shortestPath == None:
        shortestPath = p
    if p["totalDistance"] < shortestPath["totalDistance"]:
        shortestPath = p """