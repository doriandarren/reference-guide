
points = [(0, 0), (2, 2)]



max_distance = 0
max_pair = None

for i, point1 in enumerate(points):
    
    print(i, point1)
    
    for point2 in points[i + 1:]:
        
        #distance = abs(x1 - x2) + abs(y1 - y2)
        distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        if distance > max_distance:
            max_distance = distance
            max_pair = (point1, point2)

print(f"The pair {max_pair} has the maximum Manhattan distance of {max_distance}.")
