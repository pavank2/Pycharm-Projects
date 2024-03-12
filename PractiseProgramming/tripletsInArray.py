# Find all distinct triplets in an array such that the sum of the three elements equals a specified number

def find_triplets(a,target):
    a.sort()

    triplets = []
    for i in range(len(a) - 2):
        j,k = i+1,len(a)-1

        current_sum = a[i] + a[j] + a[k]
        while j < k:
            if current_sum == target:
                triplets.append([a[i],a[j],a[k]])
                j += 1
                k -= 1
            elif current_sum < target:
                j += 1
            else:
                k -= 1
    return triplets


a = [3,4,1,5,6,3,8,0]
target = 9
print(find_triplets(a,target))