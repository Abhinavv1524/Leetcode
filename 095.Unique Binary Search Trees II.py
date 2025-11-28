class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        from functools import lru_cache
        
        @lru_cache(None)
        def build(lo, hi):
            if lo > hi:
                return [None]
            res = []
            for root in range(lo, hi + 1):
                left = build(lo, root - 1)
                right = build(root + 1, hi)
                for l in left:
                    for r in right:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res
        
        return build(1, n)
