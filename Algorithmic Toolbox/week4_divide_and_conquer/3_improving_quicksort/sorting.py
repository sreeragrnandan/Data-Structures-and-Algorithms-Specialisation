# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    p_l = i = l
    p_e = r
    while i<=p_e:
        if a[i]<x:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == x:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
    return (p_l, p_e)

def partition2(a, l, r):
    x = a[l]
    p_l = i = left
    p_e = j = right
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j1 += 1
            j2 += 1
            a[i], a[j1] = a[j1], a[i]
        elif a[i] == x:
            j2 += 1
        else:
            a[l], a[j1] = a[j1], a[l]
    return (j1, j2)


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l,r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


# if __name__ == '__main__':
    # input = sys.stdin.read()
n = int(input()) 
a = list(map(int, input().split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')