class linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def reverse(head):
    prev=None
    current=head
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev

def printList(head):
    current = head
    while current:
        print(current.data, end=' -> ')
        current = current.next
    print("NULL")

node1 = linkedlist(1)
node2 = linkedlist(2)
node3 = linkedlist(3)
node1.next = node2
node2.next = node3

print("Original list:")
printList(node1)

reversed_head = reverse(node1)

print("Reversed list:")
printList(reversed_head)

