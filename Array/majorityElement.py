class Solution(object):
    def majorityElement(self, nums):
        """
        Function to find the majority element in the array.
        A majority element is an element that appears more than ⌊n/2⌋ times.
        Assumes that such an element always exists in the array.
        
        Uses the Boyer-Moore Voting Algorithm — O(n) time, O(1) space.
        """

        # Step 1: Initialize the first element as a candidate with count 1
        candidate = nums[0]
        count = 1

        # Step 2: Iterate through the rest of the elements
        for num in nums[1:]:
            if num == candidate:
                # If the current number is the same as candidate, increment count
                count += 1
            else:
                # Otherwise, decrement count
                count -= 1

                # If count drops to 0, choose a new candidate
                if count == 0:
                    candidate = num
                    count = 1

        # Step 3: Return the majority element found
        return candidate
