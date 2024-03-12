# Moves negatives to end in an array while maintaining order
def moveNegatives(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        # Find the first negative element from the left
        while left <= right and arr[left] >= 0:
            left += 1

        # Find the first non-negative element from the right
        while left <= right and arr[right] < 0:
            right -= 1

        # Swap the found elements
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


    print(arr)
a = [2,-2,1,-4,7,-6,-8,3,20,32]
moveNegatives(a)