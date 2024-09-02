class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def insert(root,data):
    if root is None:
        return Node(data)
    if root.data > data:
        root.left =  insert(root.left,data)
    else: 
        root.right = insert(root.right,data)
    return root

def bst_comp(root1,root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None and root2 != None:
        return False
    elif root1 != None and root2 == None:
        return False
    elif root1.data != root2.data:
        return False
    else:
        return ((root1.data == root2.data) and bst_comp(root1.left, root2.left)and bst_comp(root1.right, root2.right))
 
#
# def printTree(M, root, col, row, height):
#     if root is None:
#         return
#     M[row][col] = root.data
#     printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
#     printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
 
 
# def TreePrinter(r):
#     h = height(r)
#     col = getcol(h)
#     M = [[0 for _ in range(col)] for __ in range(h)]
#     printTree(M, r, col//2, 0, h)
#     for i in M:
#         for j in i:
#             if j == 0:
#                 print(" ", end=" ")
#             else:
#                 print(j, end=" ")
#         print("")
 

r = None
r = insert(r,10)
r = insert(r,5)
r = insert(r,20)
r = insert(r,15)
r = insert(r,30)
r1 = None
r1 = insert(r1,10)
r1 = insert(r1,20)
r1 = insert(r1,15)
r1 = insert(r1,30)
r1 = insert(r1,5)
r2 = None
r2 = insert(r2,10)
r2 = insert(r2,15)
r2 = insert(r2,30)
r2 = insert(r2,20)
r2 = insert(r2,5)
print(bst_comp(r,r1))
print(bst_comp(r,r2))
#TreePrinter(r)