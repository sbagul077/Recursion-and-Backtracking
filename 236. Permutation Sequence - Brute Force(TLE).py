class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = ""
        result = list()

        for i in range(1, n + 1):
            s += str(i)

        self.helper(s, 0, result)
        result.sort()
        return result[k - 1]

    def helper(self, s: str, index: int, result: list([str])) -> None:
        if index == len(s):
            result.append(s)
            return

        for i in range(index, len(s)):
            s = self.swap(s, i, index)
            self.helper(s, index + 1, result)
            s = self.swap(s, i, index)

    def swap(self, s: str, left: int, right: int) -> str:
        s = list(s)
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        return "".join(s)


if __name__ == "__main__":
    n = 9
    k = 278082
    obj = Solution()
    print(obj.getPermutation(n, k))

# For loop recursion Time Complexity: O(n! * n) + O(n! Logn!). O(n!) as we are generating every possible permutation
# and O(n) time required to make deep copy and store every sequence in the data structure. O(n! logn!) for sorting
# the result array
# Space Complexity:O(n). size of the result array
