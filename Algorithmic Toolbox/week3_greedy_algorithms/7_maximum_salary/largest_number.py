#Uses python3

import sys
# def IsGreaterOrEqual(digit, maxDigit):
#     digit = str(digit)
#     maxDigit = str(maxDigit)
#     nd = len(digit)
#     i = 0
#     j = 0
#     nm = len(maxDigit)
#     while i < nd or j < nm:
#         # print("i,j" ,i,j)
#         if i == nd:
#             i = nd - 1
#         if j ==  nm:
#             j = nm - 1
#         if digit[i] > maxDigit[j]:
            
#             # print("digit[i], maxDigit[j]",digit[i], maxDigit[j])
#             return True
#         if i < nd:
#             i += 1
#         if j < nm:
#             j += 1
#     return False

def IsGreaterOrEqual(a, b):
    return (b+a > a+b)

def largest_number(a):
    #write your code here
    res = ""
    n = len(a)
    for i in range(1,n):
        for j in range(n-1):
            if IsGreaterOrEqual(a[j], a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

    return res.join(map(str, a))

# if __name__ == '__main__':
# input = sys.stdin.read()
n =  int(input())
data = list(input().split())
print(largest_number(data))
    
