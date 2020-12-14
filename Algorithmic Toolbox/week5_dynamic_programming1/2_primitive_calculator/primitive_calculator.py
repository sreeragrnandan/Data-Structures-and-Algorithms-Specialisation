# Uses python3

def optimal_sequence(n):
    v = [0]*(n+1)
    # v[1] = 1
    for i in range(1,n+1):
        v[i] = v[i-1] + 1
        if i%2 == 0: v[i] = min(1+v[i//2], v[i])
        if i%3 == 0: v[i] = min(1+v[i//3], v[i])
    print(v)
    i = n
    sequence = []
    
    while i>1:
        sequence.append(i)
        if (v[i-1] == v[i]-1): i = i-1
        elif(i%2 == 0 and (v[i//2] == v[i]-1)): i = i//2
        elif(i%3 == 0 and (v[i//3] == v[i]-1)): i = i//3
    sequence.append(1)
    return reversed(sequence)
   
n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
