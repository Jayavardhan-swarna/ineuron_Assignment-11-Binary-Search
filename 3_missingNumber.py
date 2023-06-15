def missingNumber(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


print(missingNumber([3, 0, 1]))  # Output: 2
print(missingNumber([0, 1]))  # Output: 2
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8
