# Uses python3
import sys

def get_change(m):
    #write your code here
    coin = [4, 3, 1]
    i = 0
    n = 0
    while m != 0:
        if coin[i] <= m:
            m -= coin[i]
            n += 1
        else:
            i += 1
    return n

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))
m = int(input())
print(get_change(m))