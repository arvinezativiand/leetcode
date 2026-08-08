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

