# Uses python3
from collections import defaultdict
def get_majority_element(a):
    d = defaultdict(int)
    for x in a:
        d[x] += 1
        if d[x] > n//2:
            return x
    return -1

# if __name__ == '__main__':
#     input = sys.stdin.read()
n = int(input())
a = list(map(int, input().split()))
if get_majority_element(a) != -1:
    print(1)
else:
    print(0)
