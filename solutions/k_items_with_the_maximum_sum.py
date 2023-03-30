class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        bag = list()
        bag.extend([1] * numOnes)
        bag.extend([0] * numZeros)
        bag.extend([-1] * numNegOnes)

        return sum(bag[:k])
