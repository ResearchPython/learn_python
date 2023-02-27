class Solution(object):
    def findMaxK(self, nums):
        ans = -1
        for num in nums:
            num_abs = abs(num)
            if -num in nums and num_abs > ans:
                ans = num_abs
        return ans


if __name__ == '__main__':
    nums = [-1, 2, -3, 3]
    print(Solution().findMaxK(nums))