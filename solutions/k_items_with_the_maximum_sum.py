class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        # we will store all of our values in a "bag"
        bag = list()

        # we add each marble to the bag in descending order so that we always pull out the highest values first
        bag.extend([1] * numOnes)
        bag.extend([0] * numZeros)
        bag.extend([-1] * numNegOnes)

        # we then return everything from the bag starting from 0 and ending at k
        return sum(bag[:k])
