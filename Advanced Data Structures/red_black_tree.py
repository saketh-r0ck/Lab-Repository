class red_black_node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'

class Red_Black_Tree():
    def __init__(self):
        self.NULL = red_black_node(0)
        self.NULL.color = 'black'
        self.NULL.right = None
        self.NULL.left = None

        self.root = self.NULL

    def inorder(self):
        self.inorder_traversal(self.root)

    def inorder_traversal(self,root):
        if root != self.NULL:
            self.inorder_traversal(root.left)
            print(str(root.data) + "(" + str(root.color) +')' + "->" ,end = ' ')
            self.inorder_traversal(root.right)

    def insertion(self,key):
        new_node = red_black_node(key)
        new_node.left = self.NULL
        new_node.right = self.NULL
        new_node.parent = None
        new_node.color = 'red'
            
        parent = None
        current = self.root
        #finding parent node to insert
        while current != self.NULL:
            parent = current
            if key < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent        #bst insertion
        if parent == None:
            self.root = new_node
            
        elif key < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        if new_node.parent == None:
            new_node.color = 0
            return

        if new_node.parent.parent == None:
            return
        self.fix_insertion(new_node)

    def fix_insertion(self,node):
        while node.parent is not None and node.parent.color == 'red':
            if node.parent.parent is None:  # Ensure grandparent exists
                break

            if node.parent == node.parent.parent.right:           #checking right child
                psib = node.parent.parent.left
                if psib.color == 'red':
                    psib.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red' 
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node =  node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
            else:
                psib = node.parent.parent.right
                if psib.color == 'red':
                    psib.color = 'black'
                    node.parent.color  = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
        
    def left_rotate(self, node):
        temp = node.right
        node.right = temp.left
        if temp.left != self.NULL:
            temp.left.parent = node
        temp.parent = node.parent
        if node.parent == None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def right_rotate(self, node):
        temp = node.left
        node.left = temp.right
        if temp.right != self.NULL:
            temp.right.parent = node
        temp.parent = node.parent
        if node.parent == None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp
#Code for printing the tree in 2D
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1


def getcol(h):
    if h == 1:
        return 1
    return getcol(h-1) + getcol(h-1) + 1
 
 
def printTree(M, root, col, row, height):
    if root is None:
        return
    M[row][col] = root.data
    printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
    printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
 
 
def TreePrinter(r):
    h = height(r)
    col = getcol(h)
    M = [[0 for _ in range(col)] for __ in range(h)]
    printTree(M, r, col//2, 0, h)
    for i in M:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print("")

if __name__ == "__main__":
    bst = Red_Black_Tree()

    bst.insertion('S')
    bst.insertion('C')
    bst.insertion('A')
    bst.insertion('R')
    bst.insertion('L')
    bst.insertion('E')
    bst.insertion('T')
    bst.insertion('I')
    bst.insertion('N')
    bst.insertion('K')
    TreePrinter(bst.root)
    bst.inorder()