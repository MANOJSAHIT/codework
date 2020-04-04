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
root=Node(int(input('enter a number'))) 
root.left=Node(int(input('enter a number'))) 
root.right=Node(int(input('enter a number'))) 
root.left.left=Node(int(input('enter a number'))) 
root.left.right=Node(int(input('enter a number')))
print('the post order traversal is ')
Postorder(root)
def printLevelOrder(root):  
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
root = Node(int(input('enter the element in binary tree '))) 
root.left = Node(int(input('enter the element in binary tree '))) 
root.right = Node(int(input('enter the element in binary tree '))) 
root.left.left = Node(int(input('enter the element in binary tree '))) 
root.left.right = Node(int(input('enter the element in binary tree '))) 
print('Level Order Traversal of binary tree is -')
printLevelOrder(root)