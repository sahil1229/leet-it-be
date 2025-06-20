class Solution(object):
    def rotate(self, nums, k):
        """
        Rotates the array to the right by k steps in-place.

        :type nums: List[int]
        :type k: int
        :rtype: None
        """

        n = len(nums)
        
        # If the array has 0 or 1 elements, no rotation is needed
        if n < 2:
            return

        # Normalize k to avoid extra rotations
        # For example, rotating by 10 in an array of size 7 is same as rotating by 3
        k %= n

        # Helper function to reverse elements in the array from index `start` to `end`
        def reverse(start, end):
            while start < end:
                # Swap elements at start and end
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements (which are now at the front)
        reverse(0, k - 1)

        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)
