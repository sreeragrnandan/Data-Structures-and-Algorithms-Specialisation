# Uses python3
import sys


# def optimal_points(segments):
#     points = {""}
#     segments.sort()
#     # print(segments)
#     minPoint = segments[0][0]
#     maxPoint = segments[0][1]
#     for i in range(len(segments)):
#         if maxPoint <= segments[i][1] and maxPoint >= segments[i][0]:
#             points.add(maxPoint)
#         elif maxPoint > segments[i][1]:
#             while maxPoint > segments[i][1] and maxPoint > minPoint:
#                 maxPoint = maxPoint - 1
#             points.add(maxPoint)
#         elif maxPoint < segments[i][0]:
#             minPoint = segments[i][0]
#             if minPoint > maxPoint:
#                 if i == n-1:
#                     points.add(minPoint)
#                 elif i < n-1:
#                     if segments[i][1] < segments[i+1][0]:
#                         points.add(minPoint)
#             maxPoint = segments[i][1]
#     return list(points)[1:]
def optimal_points(segments):
    segments.sort(key = lambda x:x[1])
    point = segments[0][1]
    points = []
    points.append(point)
    for i in range(1,len(segments)):
        if point < segments[i][0] or point > segments[i][1]:
            point = segments[i][1]
            points.append(point)
    return points
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     points = optimal_points(segments)
#     print(len(points))
#     print(*points)

n = int(input())
segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))
points = optimal_points(segments)
print(len(points))
print(*points)