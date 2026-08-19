from typing import Optional


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return [z for x in range(len(nums)) for y in range(x+1, len(nums)) if (nums[x] + nums[y] == target) for z in (x, y)]


lst = Solution()
#print(lst.twoSum([3, 3], 6))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)
            
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)

class Solution3:
    def romanToInt(self, s: str) -> int:
        roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}

        int_sum = 0
        for i in range(len(s)):
            if i<len(s)-1 and roman_num[s[i]] < roman_num[s[i+1]]:
                int_sum -= roman_num[s[i]]
            else:
                int_sum += roman_num[s[i]]

        return(int_sum)

#solution = Solution3()
#print(solution.romanToInt('III'))
#print(solution.romanToInt('LVIII'))
#print(solution.romanToInt('MCMXCIV'))

class Solution4:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

solution = Solution4()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))