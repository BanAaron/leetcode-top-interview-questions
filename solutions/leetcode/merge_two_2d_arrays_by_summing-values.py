class Solution:
    def mergeArrays(
        self, numbers1: list[list[int]], numbers2: list[list[int]]
    ) -> list[list[int]]:
        from collections import defaultdict

        # we will store our values in a defaultdict
        store = defaultdict(int)

        # merge out lists together so we have one nice and clean for loop
        merged = numbers1 + numbers2

        # loops through our merged list adding the key and values as we go
        # because store is a default-dict, if the key does not exist it is automatically added
        for x in merged:
            store[x[0]] += x[1]

        # list comprehension to return a 2d list where [k=store.keys, v=store.values]
        return sorted([[k, v] for k, v in store.items()])


if __name__ == "__main__":
    s = Solution()
    print(s.mergeArrays(numbers1=[[2, 4], [3, 6], [5, 5]], numbers2=[[1, 3], [4, 3]]))
