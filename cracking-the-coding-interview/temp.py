def checkBST(root):
    def checkleft(n):
        if n.left == None:
            return True
        else:
            print n.left.data
            if not checkleft(n.left):
                return False
            if n.left.data < n.data:
                return True
            elif n.left.data == n.data:
                return False
            elif n.left.data > n.data:
                return False

    def checkright(n):
        if n.right == None:
            return True
        else:
            print n.right.data
            if not checkright(n.left):
                return False
            if n.right.data < n.data:
                return True
            elif n.right.data == n.data:
                return False
            elif n.right.data > n.data:
                return False

    return checkleft(root) and checkleft(root)