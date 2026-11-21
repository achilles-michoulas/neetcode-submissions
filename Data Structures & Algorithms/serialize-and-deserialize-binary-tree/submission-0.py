# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # ','.join()
        out = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                out.append('N')
            else:
                out.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return ','.join(out)  

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        i = 0

        def dfs():
            nonlocal i    

            val = vals[i]
            i += 1
            
            if val == 'N':
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()


        

        
