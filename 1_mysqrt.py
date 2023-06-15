def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # This line should never be reached

  
print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2
