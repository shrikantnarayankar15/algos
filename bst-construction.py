class bst:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while True:
            if value > self.value:
                if current.right is None:
                    current.right = bst(value)
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = bst(value)
                    break
                else:
                    current = current.left
        return self
    
    def getminvalue(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value
    
    

    def remove(self, value, parentnode=None):
        current = self
        while current is not None:
            if value > current.value:
                parentnode = current
                current = current.right
            elif value < current.value:
                parentnode = current
                current = current.left
            else:
                if current.left is not None and current.right is not None:
                    current.value = current.right.getminvalue()
                    current.right.remove(value, current)
                elif parentnode is None:
                    if current.right is None:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.left is None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        current.value = None
                elif parentnode.left == current:
                    parentnode.left = current.left if current.right is None else current.right
                elif parentnode.right == current:
                    parentnode.right = current.right if current.left is None else current.left
                break
        return self
                

    def prints(self):
        q = []
        q.append(self)
        while q:
            p = q.pop()
            print("",p.value)
            if p.right:
                q.append(p.right)
            if p.left:
                q.append(p.left)


w = bst(10)
w.insert(5).insert(20).insert(15).insert(21).insert(1)
w.prints()
w.remove(1).remove(10)
w.prints()