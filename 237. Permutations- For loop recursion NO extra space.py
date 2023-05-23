from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return nums

        result = list()

        self.helper(nums, 0, result)
        return result

    def helper(self, nums: list[int], index: int, result: list[list[int]]) -> None:
        if index == len(nums):
            result.append(nums.copy())
            return

        for i in range(index, len(nums)):
            self.swap(nums, i, index)
            self.helper(nums, index + 1, result)
            self.swap(nums, index, i)

    def swap(self, nums: list[int], left: int, right: int) -> None:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp


# For Loop recursion, No extra space
# Time Complexity: O(n! * n)
# Space Complexity: O(1)

nums = [1, 2, 3]
if __name__ == "__main__":
    obj = Solution()
    print(obj.permute(nums))
