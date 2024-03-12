#Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#Koko can decide her bananas-per-hour eating speed of k.
#Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#Return the minimum integer k such that she can eat all the bananas within h hours.

import math
def eating_speed(a,h):
    a.sort()

    low = 1
    high = max(a)

    while (low <= high):
        current_speed = low + (high - low)/2

        hours_spent = 0
        for item in a:
            if calculate_hours(current_speed,a,h):
                high = current_speed

            else:
                low = current_speed + 1

    return math.floor(low)
def calculate_hours(speed,a,h):
    hours_spent = 0
    for item in a:
        hours_spent += item / speed

        if item % speed > 0:
            hours_spent += 1

    if (hours_spent < h):
        return True
    else:
        return False


piles = [30,11,23,4,20]
h = 6
print(eating_speed(piles,h))