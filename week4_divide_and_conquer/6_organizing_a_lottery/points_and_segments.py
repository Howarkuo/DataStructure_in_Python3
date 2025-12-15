# from sys import stdin


# def points_cover_naive(starts, ends, points):
#     assert len(starts) == len(ends)
#     count = [0] * len(points)

#     for index, point in enumerate(points):
#         for start, end in zip(starts, ends):
#             if start <= point <= end:
#                 count[index] += 1

#     return count


# if __name__ == '__main__':
#     data = list(map(int, stdin.read().split()))
#     n, m = data[0], data[1]
#     input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
#     input_points = data[2 * n + 2:]

#     output_count = points_cover_naive(input_starts, input_ends, input_points)
#     print(*output_count)


def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    # Event types: start=1, point=2, end=3 (order matters for boundary cases)
    # We want start processed before point, and point before end? 
    # Usually: start(+1), point(query), end(-1). 
    # If inclusive: start <= point <= end. 
    # Order: start < point < end logic applies for same coordinate?
    # Better mapping: left-bound (-1), point (0), right-bound (1)
    # Actually sorting order: coordinate asc, then type.
    # Type priority for inclusive: Left (-1), Point (0), Right (1) -- Wait.
    # To include start and end: 
    # Left segment starts: type 1
    # Point appears: type 2
    # Right segment ends: type 3
    # If coords equal: Left(1) processed before Point(2) processed before Right(3)?
    # No, to count 'inside', we process Start first. When Point comes, we count. 
    # If End comes at same coord, we should count it as still active?
    # Correct order for inclusive: Start(l), Point(p), End(r). 
    # If l=p=r: Start adds 1, Point reads 1, End removes 1. 
    # So Start -> Point -> End priority.
    
    data = []
    for s in starts: data.append((s, 1)) # 1 for start
    for e in ends:   data.append((e, 3)) # 3 for end
    for i, p in enumerate(points): data.append((p, 2, i)) # 2 for point
    
    data.sort()
    
    current_segments = 0
    for entry in data:
        if entry[1] == 1:
            current_segments += 1
        elif entry[1] == 3:
            current_segments -= 1
        else:
            count[entry[2]] = current_segments
            
    return count