# Find the next greater element for each number in an array

def next_greater(a):
    l = len(a)
    greater_arr = [-1]*l # Initialize
    stack = []

    for i in range(len(a)):

        while stack and a[i] > a[stack[-1]]: # if stack is not empty and current element is greater than element on top of stack
            index = stack.pop()   # then the current element is the next greater number for the index in the stack
            greater_arr[index] = a[i]

        stack.append(i)
    return greater_arr

a = [3, 1,2, 4, 50, 20, 18, 80, 70]
print(next_greater(a))