#python code for post order traversal and level order search
class Node:
    def __init__(self,key): 
            self.left = None
            self.right = None
            self.val = key
def Postorder(root): 
    if root:  
        Postorder(root.left)  
        Postorder(root.right)  
        print(root.val)
root=Node('A')
root.left=Node('B')
root.right=Node('U')
root.left.left=Node('S')
root.left.right=Node('R')
root.right.left=Node('E')
root.right.right=Node('P')
root.left.left.left=Node('W')
root.left.left.left.left=Node('Z')
root.left.right.left=Node('Y')
root.left.right.right=Node('A')
root.right.right.left=Node('G')
root.right.right.right=Node('J')
print('the post order traversal is ')
Postorder(root)
def LevelOrder(root):  
    if root is None: 
        return 
    queue = [] 
    queue.append(root) 
    while(len(queue) > 0):  
        print(queue[0].val) 
        node = queue.pop(0) 
        if node.left is not None: 
            queue.append(node.left) 
        if node.right is not None: 
            queue.append(node.right)  
print('Level Order Traversal of binary tree is -')
LevelOrder(root)