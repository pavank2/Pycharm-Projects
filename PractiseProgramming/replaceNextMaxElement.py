#Given an array arr, replace every element in that array with the greatest
#element among the elements to its right, and replace the last element with -1

def nextMaxElement(arr):
    n = len(arr)
    max_right = -1  # Initialize the maximum value to the right as -1 for the last element

    for i in range(n - 1, -1, -1):
        current_element = arr[i]
        arr[i] = max_right  # Update the current element with the maximum value to its right
        max_right = max(max_right, current_element)  # Update the maximum value to the right


    print(arr)
a = [17,18,96,4,56,3,36,48,1]
nextMaxElement(a)


