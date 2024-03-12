#Remove duplictes from sorted array
def remove_duplicates(arr):
    i=0
    j=0
    while j < len(arr):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i=i+1
        j += 1

    #while i+1 < len(arr):
     #  arr[i+1] = ""
      # i=i+1
    return arr[:i+1]

# Example usage:
my_array = [1,2,2,2,3,4,4,4,4,5]
unique_array = remove_duplicates(my_array)
print(f"Array with duplicates removed: {unique_array}")