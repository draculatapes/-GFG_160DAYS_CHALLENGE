class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        inorder_index={val: idx for idx,val in enumerate(inorder)}
        self.preorder_index=0
        def construct(left,right):
            if left>right:
                return None
            node_val=preorder[self.preorder_index]
            curr_node=Node(node_val)
            self.preorder_index+=1
            pivot_index=inorder_index[node_val]
            curr_node.left=construct(left,pivot_index-1)
            curr_node.right=construct(pivot_index+1,right)
            return curr_node
        return construct(0,len(inorder)-1)
            
