# Smallest length of a contiguous subarray of which the sum is greater than or equal to a specified value

# Not working fully.

def cont_subarray(a,target):

   i,curr_sum,sum,start = 0,0,0,0
   curr_len = []
   min_len = len(a) + 1
   while i < len(a):
       if a[i] >= target:
           return 1
       i += 1

   i=0
   while i < len(a):
        curr_sum += a[i]

        if curr_sum < sum:
            start = i + 1
            curr_sum = 0
            sum = 0
        else:
            sum = curr_sum

        while curr_sum >= target:
            end = i
            curr_sum -= a[start]

            start += 1
            min_len = min(min_len,start-end)

        i += 1

   print(curr_len)
   return min_len

a = [2,-8, 3,1, 5,3 -7, 2, 6]
target = 8
print(f"Size of smallest continuous subarray: {cont_subarray(a,target)}")

# This works for non-negative numbered array
'''
   def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # initialize pointers and sum
        left, right, total = 0, 0, 0
        # initialize minimum length to be the length of the array plus 1 (invalid)
        min_len = len(nums) + 1
        
        # loop through the array
        while right < len(nums):
            # add current number to the sum
            total += nums[right]
            # move right pointer
            right += 1
            
            # check if the sum is greater than or equal to target
            while total >= target:
                # update minimum length if necessary
                min_len = min(min_len, right - left)
                # subtract left number from the sum and move left pointer
                total -= nums[left]
                left += 1
        
        # if minimum length is still the initialized value, there is no valid subarray
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len

'''

