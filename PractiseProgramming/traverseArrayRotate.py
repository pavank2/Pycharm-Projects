def traverse_array_circular(arr):
    n = len(arr)

    for i in range(n):
        rotated_index = (n - 1 + i) % n
        print(arr[rotated_index])

# Example usage:
input_array = [1, 2, 3, 4, 5]
print("Original Array:", input_array)

print("Traversing Array Circularly:")
traverse_array_circular(input_array)