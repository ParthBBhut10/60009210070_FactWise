from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i < len(nums) - 2 and nums[i] == nums[i+1]:
                continue
            nums[k] = nums[i]
            k += 1
        return k


if __name__ == '__main__':
    r = Solution()
    print(r.removeDuplicates([1, 1, 2]))
    print(r.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
