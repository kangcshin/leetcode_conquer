'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Loop through the list
		# The idea is to mark all positions appears in the nums as negative
		# Those that are positive means they are the missing positions
        for i in nums:
			# Calculate the position from the item in nums (For example a [4] item indicates position 3)
			# This is to avoid overflow since the item inside the array run from 1 to len(arr), not 0 -> len(arr) - 1 like the index
            index = abs(i) - 1
			
			# Mark the item occupying the existing position as negative
            nums[index] = abs(nums[index])*-1
			
		# Create a result list
        res = []
		
		# Check which position in the nums array has a positive item
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res