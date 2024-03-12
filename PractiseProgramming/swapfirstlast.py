# Python program to interchange first and last elements in a list

def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

# Check element in list
i = 35
if i in newList:
    print("Element found")
else:
    print("Element not found")
