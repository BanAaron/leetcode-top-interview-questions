# Code Challenges

My solutions to [Leetcode top interview questions](https://shorturl.at/rCMR3). Python is my language of choice 🐍. 
Comments explaining each solution are in the corresponding `solutions/something.py` file. You can click on `Solution` 
in each section to jump directly to the file.

`<<<<<<:>~`

## Two Sum

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/two-sum/)

Two Sum is a problem in where you are given an array of integers `nums` and an integer `target`, then return indices of
the two numbers such that they add up to `target`.

You may assume that:

1.  Each input would have exactly one solution.
2.  You may not use the same element twice.
3.  You can return the answer in any order.

### [Solution](solutions/two_sum.py)

<details>

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        store = {}

        for index, number in enumerate(nums):
            if target - number in store:
                return [store[target - number], index]
            else:
                store[number] = index
```

</details>

## Roman to Integer

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/roman-to-integer/)

Given a roman numeral, convert it to an integer.

```text
Symbol       Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000
```

### [Solution](solutions/roman_to_int.py)

<details>

```python
class Solution:
    def __init__(self):
        self.answer = 0

    def romanToInt(self, s: str) -> int:
        chars = s

        def add(number):
            self.answer += number

        # inelegantly replace all the edge special cases with simplified versions. IV (4) becomes IIII (1,1,1,1) etc
        chars = (
            chars.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )

        # basically a switch statement to map each possible roam-nc numeral to an integer value and add it up
        for char in chars:
            match char:
                case "I":
                    add(1)
                case "V":
                    add(5)
                case "X":
                    add(10)
                case "L":
                    add(50)
                case "C":
                    add(100)
                case "D":
                    add(500)
                case "M":
                    add(1000)

        return self.answer
```

</details>

## Longest Common Prefix

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

### [Solution](solutions/longest_common_prefix.py)

<details>

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = min(len(i) for i in strs)
        stack = set()
        result = ""

        for index in range(0, length):
            for string in strs:
                stack.add(string[index])
            if len(stack) == 1:
                result += stack.pop()
        return result
```

</details>

## Valid Parentheses

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is
valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### [Solution](solutions/valid_parentheses.py)

<details>

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        valid_brackets = ("()", "[]", "{}")

        for char in s:
            stack += char
            if char in ")]}":
                if stack[len(stack) - 2:] in valid_brackets:
                    stack = stack[:-2]

        return len(stack) == 0
```

</details>

## Merge Two Sorted Lists

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/merge-two-sorted-lists/)

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### [Solution](solutions/merge_two_sorted_lists.py)

<details>

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        new_list = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next

            new_list = new_list.next

        if list1 is not None:
            new_list.next = list1
        else:
            new_list.next = list2

        return dummy.next
```

</details>

## Remove Duplicates from Sorted Array

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements
in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were
- present in `nums` initially. The remaining elements of nums are not important as well as the size of `nums`.
- Return `k`.

### [Solution](solutions/remove_duplicates_from_sorted_array.py)

<details>

```python
class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
```

</details>

## Find the Index of the First Occurrence in a String

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1`
if `needle` is not part of `haystack`.

### [Solution](solutions/find_the_index_of_the_first_occurrence_in_a_string.py)

<details>

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

</details>

## Plus One

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/plus-one/)

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of
the integer. The digits are ordered from most significant to the least significant in left-to-right order. The large
integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

### [Solution](solutions/plus_one.py)

<details>

```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits
```

</details>

## sqrt(x)

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/sqrtx/)

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned 
integer should be non-negative as well.

You must not use any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

### [Solution](solutions/sqrt.py)

<details>

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        last_guess = x / 2.0
        while True:
            guess = (last_guess + x / last_guess) / 2
            if abs(guess - last_guess) < 0.000001:
                return int(guess)
            last_guess = guess
```

</details>

## Climbing Stairs

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/climbing-stairs/)

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### [Solution](solutions/climbing_stairs.py)

<details>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a = (1, 2)
        for i in range(3, n + 1):
            a = (a[1], a[0] + a[1])
        return a[1]
```

</details>

## Merge Sorted Array

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/merge-sorted-array/)

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, 
representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. 
To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be 
merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

### [Solution](solutions/merge_sorted_array.py)

<details>

```python
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])
```

</details>

## Binary Tree Inorder Traversal

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

Given the `root` of a binary tree, return the inorder traversal of its nodes' values. 

Example:

![Binary tree example: 1 -> 2 -> 3](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg "Binary Tree Diagram")

returns `[1, 3, 2]`

### [Solution](solutions/binary_tree_inorder_traversal.py)

<details>
    
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> list[int]:
        res = []
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)

            root = node.right
```

</details>

## Maximum Depth of Binary Tree

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest 
leaf node.

### [Solution](solutions/maximum_depth_of_binary_tree.py)

<details>

```python
    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

</details>

## Pascal's Triangle

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/pascals-triangle/description/)

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![Pascal's Triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif "A gift showing the process to solve Pascal's Triangle")

### [Solution](solutions/pascals_triangle.py)

<details>

```python
class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        result = [[1]]

        for x in range(num_rows - 1):
            temp_list = [0] + result[-1] + [0]
            next_row = []
            for j in range(len(result[-1]) + 1):
                next_row.append(temp_list[j] + temp_list[j + 1])
            result.append(next_row)

        return result
```

</details>


## Best Time to Buy and Sell Stock

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### [Solution](solutions/best_time_to_buy_and_sell_stock.py)

<details>

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_purchase)
            min_purchase = min(min_purchase, price)

        return max_profit
```

</details>

## Valid Palindrome

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/valid-palindrome/description/)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### [Solution](solutions/valid_palindrome.py)

<details>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(filter(str.isalnum, s))).lower()
        return s == s[::-1]
```

</details>

## Single Number

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/single-number/description/)

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

### [Solution](solutions/single_number.py)

<details>

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        return [int(x) for x in count if count[x] != 2][0]
```

</details>

## Majority Element

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/majority-element/)

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element 
always exists in the array.

### [Solution](solutions/majority_element.py)

<details>

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        return [x for x in count if count[x] > len(nums) / 2][0]
```

</details>

## Excel Sheet Column Number

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/excel-sheet-column-number/)

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return its corresponding 
column number.

For example:

```text
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

### [Solution](solutions/title_to_number.py)

<details>

```python
class Solution:
    def titleToNumber(self, column_title: str) -> int:
        from string import ascii_uppercase
        from collections import defaultdict
        score = 0
        letter_values = defaultdict()

        for i, char in enumerate(ascii_uppercase):
            letter_values[char] = i + 1

        for i, char in enumerate(column_title[::-1]):
            if i == 0:
                score += letter_values[char]
            else:
                score += letter_values[char] * 26 ** i

        return score
```

</details>

## Reverse Bits

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/reverse-bits/)

Reverse bits of a given 32 bits unsigned integer.

### [Solution](solutions/reverse_bits.py)

<details>

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = str(n).zfill(32)
        n = n[::-1]
        return int(n, 2)
```

</details>

## Reverse String 

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/reverse-string/)

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

### [Solution](solutions/reverse_string.py)

<details>

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = reversed(s)
```

</details>

## Fizz Buzz

![easy](https://img.shields.io/badge/-easy-brightgreen "Difficulty tag")

### [Problem](https://leetcode.com/problems/fizz-buzz/)

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

### [Solution](solutions/fizz_buzz.py)

<details>

```python
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        rules = {3: "Fizz", 5: "Buzz"}

        for x in range(1, n + 1):
            answer = ""
            for key, value in rules.items():
                if x % key == 0:
                    answer += value
            result.append(answer or str(x))
            
        return result
```

</details>
