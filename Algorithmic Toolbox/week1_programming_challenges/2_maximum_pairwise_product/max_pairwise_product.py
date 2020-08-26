# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_num1 = 0
    for i in range(n):
        if numbers[i] > max_num1:
            max_index1 = i
            max_num1 = numbers[i]
    max_num2 = 0
    for i in range(n):
        if numbers[i] > max_num2 and i != max_index1:
            max_num2 = numbers[i]

    max_product = max_num1 * max_num2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
