
#            x1,y1  x2,y2
vertices = ((1, 1), (4, 1), (4, 5))
# Formula: Area = 1/2 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|


(x1, y1),(x2, y2),(x3, y3) = vertices

area = 1/2 * abs(
    x1 * (y2 - y3) +
    x2 * (y3 - y1) +
    x3 * (y1 - y2)
)

print(area)
