# Node is defined as
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if (node==None):
            self.root = Node(value)
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = Node(value)
                else:
                    self.addNode(node.left, value)
            else:
                if(node.right==None):
                    node.right = Node(value)
                else:
                    self.addNode(node.right, value)

    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)               


def checkBST(root):
    if root == None :
        return True
    print root.data
    if root.left != None and root.data < root.left.data:
        return False
    if root.right != None and root.data > root.right.data:
        return False
    if not checkBST(root.left) and not checkBST(root.right):
        return False
    return True

if __name__ == "__main__":
    global testTree 
    testTree= Tree()
    testTree.addNode(testTree.root, 4)
    testTree.addNode(testTree.root, 2)
    testTree.addNode(testTree.root, 6)
    testTree.addNode(testTree.root, 1)
    testTree.addNode(testTree.root, 3)
    testTree.addNode(testTree.root, 5)
    testTree.addNode(testTree.root, 7)
    testTree.addNode(testTree.root, 7)
    print testTree.root.data
    print checkBST(testTree.root)