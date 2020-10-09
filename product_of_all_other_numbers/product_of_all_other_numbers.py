'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    length = len(arr)

    left, right, answer = [0] * length, [0] * length, [0] * length

    left[0] = 1

    for i in range (1, len(arr)):
        left[i] = arr[i - 1] * left[i - 1]

    right[length - 1] = 1

    for i in reversed(range(length - 1)):
        right[i] = arr[i + 1] * right[i + 1]

    for i in range(length):
        answer[i] = right[i] * left[i]

    return answer


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
