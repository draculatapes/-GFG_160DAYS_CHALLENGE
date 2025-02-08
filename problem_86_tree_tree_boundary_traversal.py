class Solution:
    def boundaryTraversal(self, root):
        # Code here
        if not root.left and not root.right:
            return [root.data]
        def boundary(node,isLeft,res):
            if not node:
                return res
            if node.left==None and node.right==None:
                return res
            res.append(node.data)
            if isLeft:
                if node.left!=None:
                    return boundary(node.left,isLeft,res)
                else:
                    return boundary(node.right,isLeft,res)
            else:
                if node.right!=None:
                    return boundary(node.right,isLeft,res)
                else:
                    return boundary(node.left,isLeft,res)
        def leafNodes(node,res):
            if node.left==None and node.right==None:
                res.append(node.data)
                return res
            if node.left!=None:
                leafNodes(node.left,res)
            if node.right!=None:
                leafNodes(node.right,res)
            return res
        res=[root.data]
        left_boundary=boundary(root.left,True,[])
        res.extend(left_boundary)
        
        #adding leaf nodes
        leafs=leafNodes(root,[])
        res.extend(leafs)
        
        right_boundary=boundary(root.right,False,[])
        right_boundary=right_boundary[::-1]
        res.extend(right_boundary)
        return res
