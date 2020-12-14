# Uses python3
import sys

def get_change(m):
    #write your code here
    minNumCoins = []
    minNumCoins.append(0)
    coins = [1, 3, 4]
    for i in range(1, m+1):
        minNumCoins.append(1000000)
        for coin in coins:
            if i >= coin:
                NumCoins = minNumCoins[i - coin] + 1
                if NumCoins < minNumCoins[i]:
                    minNumCoins[i] = NumCoins
    return minNumCoins[m]

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))
m = int(input())
print(get_change(m))