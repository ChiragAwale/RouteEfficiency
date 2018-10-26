
class CNode:
    def __init__(self,name):
        self.name = name
        self.nextNodeList=[]


def addNextNode(previousNode, newNode,value):
    item = [newNode,value]
    previousNode.nextNodeList.append(item)

def insertNewNode(previousNode, name, value):
    currentNode = previousNode
    currentNode.nextNode = CNode(name)
    addNextNode(currentNode,currentNode.nextNode,value)
    return currentNode.nextNode


# def deleteNode(head, valueToDelete):
#     currentNode = head
#     previousNode = None
#     while currentNode is not None:
#         if currentNode.value == valueToDelete:
#             if previousNode is None:
#                 newHead = currentNode.nextNode
#                 currentNode.nextNode = None
#                 return newHead
#             previousNode.nextNode = currentNode.nextNode
#             return head
#         previousNode = currentNode
#         currentNode = currentNode.nextNode
#     return head




