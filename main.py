from cNodeList import *

cNodeDict={}


while(True):
    print("Enter  First Point")
    source = input()

    print("Enter Second Point")
    destination = input()


    print("Enter Value")
    value = input()

    # For Avoiding Duplicate Values
    sKey = source.upper()
    dKey = destination.upper()


    if sKey not in cNodeDict:
        sNode = CNode(source)
        cNodeDict.update({source.upper(): sNode})
    else:
        sNode = cNodeDict.get(sKey)

    if dKey not in cNodeDict:
            dNode = insertNewNode(sNode, destination, value)
            cNodeDict.update({destination.upper(): dNode})
    else:
        addNextNode(sNode,cNodeDict.get(dKey),value)



    print("Enter more? [y//n]")
    choice = input()
    if choice.lower() == "n":
        break



#Traversing
currentNode = cNodeDict.get("A")
print(currentNode.nextNodeList)

for item in currentNode.nextNodeList:
    print("Name " + item[0].name)
    print("Value " + item[1])
    for subItem in item[0].nextNodeList:
        print(subItem)
