class MyNode: 
    def __init__(self,value):
        self.value = value
        self.next = None
        
class MyList:
    def __init__(self):
        self.head = None
        
    def append(self,value):
        if self.head != None:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = MyNode(value)
        else:
            self.head = MyNode(value)


class MyListMod(MyList):
    
    def met(self,x):
        if self.head != None:
            curr = self.head
            c = 0
            while curr.next != None and c < x:
                c += 1
                curr = curr.next
            if c == x:
                return curr.value
            else:
                raise Exception
        else:
            raise Exception


