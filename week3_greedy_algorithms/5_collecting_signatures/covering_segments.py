from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    segments.sort(key=lambda x: x[1])
    
    points = []
    current_point = segments[0][1]
    points.append(current_point)
    
    for s in segments:
        if current_point < s[0] or current_point > s[1]:
            current_point = s[1]
            points.append(current_point)
            
    return points
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    # return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
