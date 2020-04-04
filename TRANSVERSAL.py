#2)python code for preorder,postorder,inorder traversal
class Node:
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
def Inorder(root):
    if root:  
        Inorder(root.left)  
        print(root.val) 
        Inorder(root.right)  
def Postorder(root): 
    if root:  
        Postorder(root.left)  
        Postorder(root.right)  
        print(root.val) 
def Preorder(root): 
    if root:  
        print(root.val),  
        Preorder(root.left)  
        Preorder(root.right) 
root = Node('A')
root.left = Node('B') 
root.right = Node('C') 
root.left.left = Node('D') 
root.left.right = Node('E') 
root.right.left=Node('F') 
print('Preorder traversal of binary tree is\n')
Preorder(root) 
print('Inorder traversal of binary tree is\n')
Inorder(root) 
print('Postorder traversal of binary tree is\n')
Postorder(root)