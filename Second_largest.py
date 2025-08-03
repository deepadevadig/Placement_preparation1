def second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second 

# Example
numbers = [4, -10, 2, 10, 3]
print("Second largest:", second_largest(numbers))
