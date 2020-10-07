'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    length = len(nums)
    max_of_each = [] 

    for i in range(length):
        plus_k = i + k
        highest = max(nums[i:plus_k])
        max_of_each.append(highest)

    return max_of_each



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
