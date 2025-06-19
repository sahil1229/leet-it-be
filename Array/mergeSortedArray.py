def mergeSort(nums1, m, nums2, n):
    # Start from the end of nums1, where we have space to merge
    p = m + n - 1        # Pointer for placement in nums1
    p1 = m - 1           # Pointer for last valid element in nums1
    p2 = n - 1           # Pointer for last element in nums2

    # Merge from the back until one of the lists is exhausted
    while p1 >= 0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]  # Place the bigger one at the end
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    # If nums2 still has elements, copy them
    # (Remaining nums1 elements are already in correct place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1
