def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


print(findPeakElement([1, 2, 3, 1]))  # Output: 2
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5
