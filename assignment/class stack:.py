class stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self,item):
        if self.items.is_empty():
            return None
        last_item=self.items[-1]
        self.items=self.items[:-1]
        return last_item
    
    def peek(self):
        if self.items.is_empty:
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    
class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue.is_empty():
            return None
        first_element=self.queue[0]
        self.queue=self.queue[1:]
        return first_element
    
    def peek(self):
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queu)==0
    
    def size(self):
        return len(self.queue)
    
class node:
    def __init__(self,data):
        self.data=data
        self.node=None
    
class linkedlist:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        newnode=node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.node:
            current=current.node
        current.node=newnode
    
    def prepend(self,data):
        newnode=node(data)
        newnode.node=self.head
        self.head=newnode


    def delete(self,data):
        current=self.head
        previous=None
        while current:
            if current.data==data:
                if previous:
                    previous.node=current.node
                else:
                    self.head=current.node
                return
            previous=current
            current=current.node
    
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.node
        print("none")






            