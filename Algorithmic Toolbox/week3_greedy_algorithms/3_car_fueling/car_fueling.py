# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    # if len(stops) == 0 and distance <= tank:
    #     return 0
    # if len(stops) == 0 and distance > tank:
    #     return -1

    NumTanks = 0
    i = 0
    stops = [0] + stops
    stops.append(distance)
    n = len(stops)

    currentStop = 0
    while currentStop < n-1:
        lastStop = currentStop
        while currentStop < n-1 and stops[currentStop + 1] - stops[lastStop] <= tank:
            currentStop += 1

        if currentStop == lastStop and currentStop != n-1:
            return -1
        if currentStop < n-1:
            NumTanks += 1

    return NumTanks

# if __name__ == '__main__':
#     d, m, _, *stops = map(int, sys.stdin.read().split())
#     print(compute_min_refills(d, m, stops))

d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))
print(compute_min_refills(d, m, stops))