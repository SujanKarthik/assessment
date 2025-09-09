class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    @staticmethod
    def printlinkedlist(head):
        if head is None:
            print("Empty linked list")
            return
        current = head
        while current:
            print(current.data)
            current = current.next

node1 = LinkedList(27)
node2 = LinkedList(28)
node3 = LinkedList(29)

node1.next = node2
node2.next = node3

LinkedList.printlinkedlist(node1)
