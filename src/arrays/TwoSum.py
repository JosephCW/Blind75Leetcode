# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
#
# Explanation: Because
# nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
#
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
from typing import List


class TwoSum:
    # Initial O(n^2) approach
    # def two_sum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == target - nums[j]:
    #                 return [i, j]

    # Approach that is less friendly to space, but is of much higher performance
    # No longer O(n^2), is O(n)
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}

        for i in range(len(nums)):
            val_to_index[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in val_to_index and val_to_index[complement] != i:
                return [i, val_to_index[complement]]


