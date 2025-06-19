def remove(nums):
    k = 1  # Index where the next unique element will be placed
    for i in range(1, len(nums)):  # Start from the second element
        if nums[i] != nums[i - 1]:  # If current element is not same as the previous one
            nums[k] = nums[i]  # Place it at index k
            k += 1  # Move k to the next position
    return k  # Return count of unique elements
