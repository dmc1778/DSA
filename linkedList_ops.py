class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def deleteLast(self):
        currentNode = self.head
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
            if currentNode.next is None:
                previousNode.next = None
                

    def delete(self, targetNode):
        if self.head is None:
            print('List is empty!')
            return
        currentNode = self.head
        
        while currentNode.next is not None:
                previousNode = currentNode
                currentNode = currentNode.next
                if self.head.data == targetNode:
                    self.head = currentNode
                if currentNode.data == targetNode:
                    previousNode.next = currentNode.next
                    currentNode.next = None
            
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            self.head = newNode
            newNode.next = tempNode

    def append(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while(True):
                if lastNode.next is None:
                    break
                # update pointer to the last node in the list
                lastNode = lastNode.next
            lastNode.next = newNode
        
    def printList(self):
        if self.head is None:
            print('List is empty!')
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next
        
firstNode = Node('Nima')
linkedList = LinkedList()
linkedList.append(firstNode)
secondNode = Node('John')
linkedList.append(secondNode)
thirdNode = Node('Ali')
linkedList.append(thirdNode)
fourthNode = Node('Jafar')
linkedList.append(fourthNode)

linkedList.delete('Ali')

# linkedList.deleteLast()


linkedList.printList()