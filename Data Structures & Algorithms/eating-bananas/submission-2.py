class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            middle = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / middle)

            if hours <= h:
                right = middle
            else:
                left = middle + 1

        return right