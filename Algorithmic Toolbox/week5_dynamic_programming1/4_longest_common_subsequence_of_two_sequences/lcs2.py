#Uses python3

import sys

def lcs2(a, b,m,n):
    #write your code here
    d = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(0,m+1):
        for j in range(0, n+1):
            if i == 0 or j == 0:
                d[i][j] = 0
            elif a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    return d[m][n]

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))

#     n = data[0]
#     data = data[1:]
#     a = data[:n]

#     data = data[n:]
#     m = data[0]
#     data = data[1:]
#     b = data[:m]

#     print(lcs2(a, b))
m = int(input())
a = list(map(int,input().split()))
n = int(input())
b = list(map(int,input().split()))
print(lcs2(a,b,m,n))