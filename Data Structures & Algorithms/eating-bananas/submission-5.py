

class Solution(object):
    import math
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left <= right:
            middle = left + (right- left) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / middle)

            if hours <= h:
                right = middle -1
            else:
                left = middle + 1
                
        return left