# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    while right >= left:
        mid = (right + left)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     m = data[n + 1]
#     a = data[1 : n + 1]
values = list(map(int, input().split()))
values.pop(0)
keys = list(map(int, input().split()))
keys.pop(0)
for x in keys:
    # replace with the call to binary_search when implemented
    print(binary_search(values, x), end = ' ')
