from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        st = list()
        result = list()
        n = len(nums)
        visited = [False] * n
        self.helper(nums, st, result, n, visited)
        return result

    def helper(self, nums: list[int], st: list[int], result: list[list[int]], n: int, visited: list[int]) -> None:
        if len(st) == n:
            result.append(st.copy())
            return

        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                st.append(nums[i])
                self.helper(nums, st, result, n, visited)
                st.pop()
                visited[i] = False


# Time Complexity :O(n! * n)
# Space Complexity:O(n) + O(n). Size of the st and height of the recursion tree

nums = [1, 2, 3]
if __name__ == "__main__":
    obj = Solution()
    print(obj.permute(nums))
