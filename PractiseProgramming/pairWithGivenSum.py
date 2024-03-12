#Pair with given sum
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen_numbers = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen_numbers:
            pairs.append((num, complement))
        seen_numbers.add(num)
    return pairs
# Example usage:
my_array = [2, 7, 4, 0, 9, 5, 1, 3]
target = 7
result = find_pairs_with_sum(my_array, target)
print(f"Pairs with sum {target}: {result}")