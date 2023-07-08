class Solution:
    def ContainDuplicates(self, arr):
        hashSet = set()

        for num in arr:
            if num in hashSet:
                return True

            hashSet.add(num)

        return False

arr = [1, 1, 2, 3]
solution = Solution()
print(solution.ContainDuplicates(arr))

