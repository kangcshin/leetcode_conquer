'''

Level - Medium

Given an array of integers `nums` and an intger `k`, 
return the total number of continuous subarrays whose sum equals to `k`.

Example 1:
Input: nums = [1, 1, 1], k = 2
Output: 2

Example 2:
Input: nums = [1, 2, 3], k = 3
Output: 2

'''

# Brute Force
class Solution:
  def subarraaySum(self, nums:List[int], k:int) -> int:
    result = 0
    for i in range(len(nums)):
      temp_sum = nums[i]
      if temp_sum == k:
        result += 1
      for j in range(i+1, len(nums)):
        temp_sum += nums[j]
        if temp_sum == k:
          result += 1
    return result
  
# Prefix_Sum
class Solution:
  def subarraaySum(self, nums:List[int], k:int) -> int:
    result = 0
    prefix_sum = collections.defaultdict(int)
    # key: prefix_sum, val: frequency
    prefix_sum[0] = 1
    cur_sum = 0
    for idx, val in enumerate(nums):
      cur_sum += val
      if cur_sum - k in prefix_sum:
        result += prefix_sum[cur_sum - k]
      prefix_sum[cur_sum] += 1
    return result
  
