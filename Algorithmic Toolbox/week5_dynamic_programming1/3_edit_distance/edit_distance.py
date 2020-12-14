# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    d = [[0 for j in range(m+2)] for i in range(n+2)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0):
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            elif s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
               d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
    
    return d[m][n]6

if __name__ == "__main__":
    print(edit_distance(input(), input()))
# s = input()
# t = input()
# print(edit_distance(s,t))