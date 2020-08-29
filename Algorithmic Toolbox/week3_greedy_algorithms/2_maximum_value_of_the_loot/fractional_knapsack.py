# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


# if __name__ == "__main__":
#     data = list(map(int, sys.stdin.read().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))
data = list(map(int, input().split()))
l = []
n = data[0]
W = data[1]
for i in range(n):
    t = list(map(int, input().split()))
    l.append([t[0]/t[1], t[1]])
l.sort(reverse=True)

TotVal = 0
i = 0
while W > 0:

    if l[i][1] == 0:
        i += 1
    if i == n:
        break
    if W >= l[i][1]:
        TotVal += l[i][0] * l[i][1]
        W -= l[i][1]
        l[i][1] = 0
    elif W < l[i][1]:
        TotVal += (l[i][0] * W)
        l[i][1] -= W
        W = 0

print("{:.10f}".format(TotVal))