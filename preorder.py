class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    @staticmethod
    def Preorder(root):
        if root is None:
            return("empty")
        print(root.data, end=' ')
        node.Preorder(root.left)
        node.Preorder(root.right)



root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
node.Preorder(root)