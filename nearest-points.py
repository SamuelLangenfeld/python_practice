class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def closest_points(points, k, p):
    # naive
    # linear? keep track of k closest points (and distance), then remove/replace
    #  as you continue. Not efficient. n * n, for each point, have to iterate on list

    # optimal
    # can sort in place, n times. So it's just one round of calculations, then a sort
    # sort complexity, n calculations + nlogn sort
    # return [(point.x, point.y) for point in points].sort(key = lambda k: distance(k))

    def distance(k):
        return abs(k.x - p.x)**2 + abs(k.y - p.y)**2
    return_list = points[:]
    return_list.sort(key=distance)
    return return_list[:k]


points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]

# list of points, num of closest points to find, starting point
print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]
