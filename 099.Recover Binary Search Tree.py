class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        x = y = prev = None
        cur = root
        
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    if prev and prev.val > cur.val:
                        y = cur
                        if not x:
                            x = prev
                    prev = cur
                    pre.right = None
                    cur = cur.right
            else:
                if prev and prev.val > cur.val:
                    y = cur
                    if not x:
                        x = prev
                prev = cur
                cur = cur.right
        
        x.val, y.val = y.val, x.val
