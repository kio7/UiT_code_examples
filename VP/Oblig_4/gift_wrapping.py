# Made in collaboration with Anders Karlskås and Jørgen Nordås

from math import sqrt

def get_convex_hull(old_points):
    # Deletes dupes, if we have dupes everything fails.
    points = []
    [points.append(n) for n in old_points if n not in points]
    polygon = []
    # Get starting point
    p0 = min(points)

    copy = points.copy()
    copy.pop(copy.index(p0))
    polygon.append(p0)

    if len(points) < 2:
        return [p0, p0]

    elif len(points) < 3:
        return [points[0], points[1], points[0]]

    x1, y1 = copy[0][0], copy[0][1] # Random P1
    copy.pop(copy.index([x1, y1]))

    while True:
        while len(copy) > 0:
            while len(copy) > 0:
                x2, y2 = copy[0][0], copy[0][1]
                res = calc_lef_rig(p0[0], p0[1], x1, y1, x2, y2)

                if res == 0: # If on the same line
                    if check_distance(p0[0], p0[1], x1, y1) <= check_distance(p0[0], p0[1], x2, y2):
                        x1, y1 = x2, y2
                        copy.pop(copy.index([x1, y1]))

                elif res < 0: # if P2 on the right
                    x1, y1 = x2, y2
                    copy.pop(copy.index([x1, y1]))

                else: # If P2 on the left
                    copy.pop(copy.index([x2, y2]))


        p0 = [x1, y1]
        # If first p0 == new p0 then break
        if polygon[0] == p0:
            return polygon

        copy = points.copy()
        copy.pop(copy.index(p0))
        x1, y1 = copy[0][0], copy[0][1] # New random P1
        copy.pop(copy.index([x1, y1]))

        polygon.append(p0)

    
def check_distance(x1, y1, x2, y2):
    return sqrt(((x1 - x2)**2) + ((y1 - y2)**2))


def calc_lef_rig(y0, x0, y1, x1, y2, x2):
    return ((x1 - x0) * (y2 - y0)) - ((x2 - x0) * (y1 - y0))

def main():
    # starting_points = [[243, 43], [281, 57], [336, 61], [311, 111], [379, 88], [371, 45], [274, 27]]

    data = [[1, 2.4], [2.5, 2], [1.5, 34.5], [5.5, 6], [6, 2.4], [5.5, 9]]
    res = get_convex_hull(data)
    print(res)
    fasit = [[2.5, 2.0], [6.0, 2.4], [5.5, 9.0], [1.5, 34.5], [1.0, 2.4]] # The one that should betaken out [5.5, 6]
    print(fasit)

if __name__ == '__main__':
    main()
