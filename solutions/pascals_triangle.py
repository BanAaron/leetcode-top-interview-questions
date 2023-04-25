class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        # we know the first entry will always be 1, so we can populate it
        result = [[1]]

        # we loop through num_rows - 1 because we've already created the first row when we declared result
        for x in range(num_rows - 1):
            # we place the last value between two zeros to make our calculation easier
            temp_list = [0] + result[-1] + [0]
            next_row = []
            for j in range(len(result[-1]) + 1):
                next_row.append(temp_list[j] + temp_list[j + 1])
            result.append(next_row)

        return result
