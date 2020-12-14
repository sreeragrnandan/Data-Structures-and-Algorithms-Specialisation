# Uses python3
import sys

def optimal_weight(W, w):
    dp_result = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n+1):
        for weight in range(1, W+1):
            dp_result[i][weight] = dp_result[i-1][weight]
            if w[i-1] <= weight:
                val = dp_result[i-1][weight - w[i-1]] + w[i-1]
                if val > dp_result[i][weight]:
                    dp_result[i][weight] = val

    # return dp_result
    print(dp_result)
    return dp_result[n][W]

# def optimal_weight(W, w):
#     result = 0
#     for i in range(len(w)):
#         if W >= w[i]:
#             print(result, "|", w[i], "|", W)
#             result += w[i]
#             W -= w[i]
#     return result  
    
# if __name__ == '__main__'
#     input = sys.stdin.read()
#     W, n, *w = list(map(int, input.split()))
#     print(optimal_weight(W, w))

def optimal_weight(W, w, n):
    d = [[0 for x in range(W+1)] for y in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            d[i][j] = d[i-1][j]
            if w[i-1] <= j:
                val =  d[i-1][j-w[i-1]] + w[i-1]
                if val > d[i][j]:
                    d[i][j] = val
    return d[n][W]

W = list(map(int, input().split()))
n = W[1]
W = W[0]
w = list(map(int, input().split()))
w.sort(reverse=True)
print(W, w)
print(optimal_weight(W, w, n))