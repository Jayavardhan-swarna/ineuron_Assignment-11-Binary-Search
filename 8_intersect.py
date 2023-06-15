def intersect(nums1, nums2):
    freq_map = {}
    result = []
    
    # Count the frequency of elements in nums1
    for num in nums1:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Find the common elements and update the frequency accordingly
    for num in nums2:
        if num in freq_map and freq_map[num] > 0:
            result.append(num)
            freq_map[num] -= 1
    
    return result


print(intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]
