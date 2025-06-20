def remove(nums):
    # Pointer 'i' keeps track of the position to insert allowed elements
    i = 0

    # Loop through each number in the input list
    for num in nums:
        # If we haven't yet added two elements, or the current number is not the same
        # as the number two positions behind, it's safe to include
        if i < 2 or num != nums[i - 2]:
            nums[i] = num  # Place the current number at the 'i'th position
            i += 1         # Move the insert pointer forward

    # Return the new length of the array with duplicates reduced
    return i
