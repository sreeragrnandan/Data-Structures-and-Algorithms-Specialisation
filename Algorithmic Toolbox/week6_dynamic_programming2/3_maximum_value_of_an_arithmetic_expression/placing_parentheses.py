import math
def calc(a, b, op):
    """ Evaluates the expression (a op b)
    (int, int, char) -> (int) """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def MinAndMax(M, m, i, j, operators):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = calc(M[i][k], M[k+1][j], operators[k])
        print(M[i][k],  operators[k] ,M[k+1][j])
        
        b = calc(M[i][k], m[k+1][j], operators[k])
        print(M[i][k], operators[k] ,m[k+1][j])

        c = calc(m[i][k], M[k+1][j], operators[k])
        print(m[i][k], operators[k] ,M[k+1][j])

        d = calc(m[i][k], m[k+1][j], operators[k])
        print(m[i][k], operators[k],m[k+1][j])

        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    print(min_value, max_value)
    print("==============================")
    return min_value, max_value


def get_max_value(operands, operators):
    n = len(operands)
    m = [[None for x in range(n)] for y in range(n)]
    M = [[None for x in range(n)] for y in range(n)]
    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]  
    print("m")
    print(m)
    print("=====================================")
    print("M")
    print(M)
    print("=====================================")
    for s in range(1, n):
        for i in range(0, n-s):
            j = i+s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)
    return M[0][n-1] 

    
expression = input()
operators, operands = [], []
for e in expression:
    if e in ['+', '-', '*']:
        operators.append(e)
    else:
        operands.append(int(e))

print(get_max_value(operands, operators))