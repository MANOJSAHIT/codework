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
root=Node(int(input('enter a number'))) 
root.left=Node(int(input('enter a number'))) 
root.right=Node(int(input('enter a number'))) 
root.left.left=Node(int(input('enter a number'))) 
root.left.right=Node(int(input('enter a number'))) 
print('Preorder traversal of binary tree is\n')
Preorder(root) 
print('Inorder traversal of binary tree is\n')
Inorder(root) 
print('Postorder traversal of binary tree is\n')
Postorder(root)