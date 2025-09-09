class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def height(root):
        if root==None:
            return -1
        
        left_height = node.height(root.left)
        right_height = node.height(root.right)
        return 1 + max(left_height, right_height)


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)

print("Height of the tree:", node.height(root))
