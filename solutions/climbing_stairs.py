class Solution:
    def climbStairs(self, n: int) -> int:
        # if n is less than three we know there can only be 1, 2 or 3 possibilities respectively
        if n <= 3:
            return n
        # store of the numbers of steps we can take
        a = (1, 2)
        for i in range(3, n + 1):
            # then we just loop through the fibonacci sequence to get our answer
            # for example (1, 2) becomes:
            #             (2, 3)
            #             (3, 5)
            #             (5, 8)
            #             ...
            a = (a[1], a[0] + a[1])
        return a[1]
