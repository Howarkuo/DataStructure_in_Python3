# from collections import namedtuple
# from itertools import combinations
# from math import sqrt


# Point = namedtuple('Point', 'x y')


# def distance_squared(first_point, second_point):
#     return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


# def minimum_distance_squared_naive(points):
#     min_distance_squared = float("inf")

#     for p, q in combinations(points, 2):
#         min_distance_squared = min(min_distance_squared,
#                                    distance_squared(p, q))

#     return min_distance_squared


# if __name__ == '__main__':
#     input_n = int(input())
#     input_points = []
#     for _ in range(input_n):
#         x, y = map(int, input().split())
#         input_point = Point(x, y)
#         input_points.append(input_point)

#     print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))



import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_d = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            if d < min_d: min_d = d
    return min_d

def strip_closest(strip, d):
    min_d = d
    strip.sort(key=lambda x: x[1]) # Sort by Y
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_d:
                break
            d_temp = dist(strip[i], strip[j])
            if d_temp < min_d:
                min_d = d_temp
    return min_d

def closest_recursive(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)
    
    mid = n // 2
    mid_point = px[mid]
    
    px_left = px[:mid]
    px_right = px[mid:]
    
    # Split Py efficiently usually required for O(nlogn), simplified here
    py_left = []
    py_right = []
    for p in py:
        if p[0] < mid_point[0] or (p[0] == mid_point[0] and p[1] < mid_point[1]): 
             # Logic needs strict alignment with px split, simplified:
             if p in px_left: py_left.append(p)
             else: py_right.append(p)
             
    # Actually simpler to just rely on recursion if N is small, 
    # but strictly we filter Py based on X split
    
    d1 = closest_recursive(px_left, py_left)
    d2 = closest_recursive(px_right, py_right)
    d = min(d1, d2)
    
    strip = [p for p in py if abs(p[0] - mid_point[0]) < d]
    return min(d, strip_closest(strip, d))

def minimum_distance(x, y):
    points = list(zip(x, y))
    points.sort(key=lambda p: p[0])
    px = points
    py = sorted(points, key=lambda p: p[1])
    return closest_recursive(px, py)
