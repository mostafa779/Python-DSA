class Node:
    
    def __init__(self,val,left=None,right=None):
        self.val  = val 
        self.left = left
        self.right = right

    def insert(self,val):
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        else:
            self.val = val

    def preOrder(self):
        if self.left:
            self.left.preOrder()
        print(self.val)
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.val)

    def inOrder(self):
        print(self.val)
        if self.left:
            self.left.inOrder()
        if self.right:
            self.right.inOrder()

    def search(self,key):
        if key < self.val:
            if self.left is None:
                return f"{key} is not found"
            return self.left.search(key)
        elif key > self.val:
            if self.right is None:
                return f"{key} is not found"
            return self.right.search(key)
        else:
            return f"{key} is found"

    def delete(self,val):
        pass


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(11)
root.insert(19)


root.preOrder()#10 11 14 19 27 31 35
print("----------------")
root.postOrder()#11 10 19 14 31 35 27
print("----------------")
root.inOrder()#27 14 10 11 19 35 31
print("----------------")
print(root.search(10))
print(root.search(100))
print("----------------")
