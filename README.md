# Code Challenges

This is a collection of programming challenges I have completed. Mainly from LeetCode, Codewarsa and interview question practice.

Python is my language of choice 🐍

`<<<<<<:>~`

---

## LeetCode

### [Add Binary](solutions/leetcode/add_binary.py)

[LeetCode 67](https://leetcode.com/problems/add-binary/)

Given two binary strings `a` and `b`, return their sum as a **binary string**.

### [Best Time to Buy and Sell Stock](solutions/leetcode/best_time_to_buy_and_sell_stock.py)

[LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### [Caesar's Cipher](solutions/leetcode/caesars_cipher.py)

Caesar's Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher 
in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

In this example we use the increment of 1. A will become B, B will be become C and so on.

### [Check Whether Two Strings are Almost Equivalent](solutions/leetcode/check_almost_equivalent.py)

[LeetCode 2068](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/)

Two strings `word1` and `word2` are considered almost equivalent if the differences between the frequencies of each 
letter from `a` to `z` between `word1` and `word2` is at **most** `3`.

Given two strings `word1` and `word2`, each of length `n`, return `true` if `word1` and `word2` are almost equivalent, or false 
otherwise.

The **frequency** of a letter `x` is the number of times it occurs in the string.

### [Count the Number of Vowel Strings in Range](solutions/leetcode/count_number_of_vowel_strings_in_range.py)

[LeetCode 2586](https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/)

You are given a 0-indexed array of string `words` and two integers `left` and `right`.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel 
characters are `'a', 'e', 'i', 'o', 'u'`.

Return the number of vowel strings `words[i]` where `i` belongs to the inclusive range `[left, right]`.

### [Find the Index of the First Occurrence in a String](solutions/leetcode/find_the_index_of_the_first_occurrence_in_a_string.py)

[LeetCode 28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` 
if `needle` is not part of `haystack`.

### [Find the Longest Balanced Substring of a Binary String](solutions/leetcode/find_the_longest_balanced_substring.py)

[LeetCode 2609](https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/)

You are given a binary string `s` consisting only of zeroes and ones.

A substring of `s` is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of `s`.

A substring is a contiguous sequence of characters within a string.

### [Fizz Buzz](solutions/leetcode/fizz_buzz.py)

[LeetCode 412](https://leetcode.com/problems/fizz-buzz/)

Given an integer n, return a string array answer (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by `3` and `5`.
- `answer[i] == "Fizz"` if `i` is divisible by `3`.
- `answer[i] == "Buzz"` if `i` is divisible by `5`.
- `answer[i] == i` (as a string) if none of the above conditions are true.

### [Form Smallest Number from Two Digit Arrays](solutions/leetcode/form_smallest_number_from_two_digit_arrays.py)

[LeetCode 2605](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/submissions/927517269/)

Given two arrays of unique digits `nums1` and `nums2`, return the **smallest** number that contains **at least** one 
digit from each array.

### [K Items With the Maximum Sum](solutions/leetcode/k_items_with_the_maximum_sum.py)

[LeetCode 2600](https://leetcode.com/problems/k-items-with-the-maximum-sum/description/)

There is a bag that consists of items, each item has a number `1`, `0`, or -`1` written on it.

You are given four non-negative integers `numOnes`, `numZeros`, `numNegOnes`, and `k`.

The bag initially contains:

- `numOnes` items with `1`s written on them.
- `numZeroes` items with `0`s written on them.
- `numNegOnes` items with `-1`s written on them.

We want to pick exactly `k` items among the available items. Return the **maximum** possible sum of numbers written on 
the items.

### [Left and Right Sum Difference](solutions/leetcode/left_right_sum_differences.py)

[LeetCode 2574](https://leetcode.com/problems/left-and-right-sum-differences/description/)

Given a **0-indexed** integer array `nums`, find a **0-indexed** integer array `answer` where:

- `answer.length == nums.length`.
- `answer[i] = |leftSum[i] - rightSum[i]|`.

`| |` means absolute value. 

Where:

- `leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, 
 `leftSum[i] = 0`.
- `rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, 
`rightSum[i] = 0`.

Return the array `answer`.

![Professionally drawn illustration](https://i.imgur.com/BK1Znxv.png)

### [Length of Last Word](solutions/leetcode/length_of_last_word.py)

[LeetCode 58](https://leetcode.com/problems/length-of-last-word/description/)

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string.

A word is a maximal substring consisting of non-space characters only.

### [Longest Common Prefix](solutions/leetcode/longest_common_prefix.py)

[LeetCode 14](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### [Maximum Count of Positive and Negative Integer](solutions/leetcode/maximum_count_of_positive_and_negative_integer.py)

[LeetCode 2529](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/submissions/928460829/)

Given an array `nums` sorted in non-decreasing order, return the **maximum** between the number of positive integers and
the number of negative integers.

### [Maximum Depth of Binary Tree](solutions/leetcode/max_depth_binary_tree.py)

[LeetCode 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest 
leaf node.

### [Maximum Difference by Remapping a Digit](solutions/leetcode/maximum_difference_by_remapping_a_digit.py)
 
[LeetCode 2566](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/)

You are given an integer `num`. You know that Danny Mittal will sneakily remap one of the `10` possible digits (0 to 9) 
to another digit.

Return the difference between the maximum and minimum values Danny can make by remapping exactly one digit in `num`.#

**Notes:**

* When Danny remaps a digit d1 to another digit d2, Danny replaces all occurrences of `d1` in num with `d2`.
* Danny can remap a digit to itself, in which case `num` does not change.
* Danny can remap different digits for obtaining minimum and maximum values respectively.
* The resulting number after remapping can contain leading zeroes.

### [Merge Two 2D Arrays by Summing Values](solutions/leetcode/merge_two_2d_arrays_by_summing-values.py)

[LeetCode 2570](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/)

You are given two **2D** integer arrays `nums1` and `nums2`.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

- Only ids that appear in at least one of the two arrays should be included in the resulting array.
- ach id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be `0`.

Return the resulting array. The returned array must be sorted in ascending order by id.

### [Number of Even and Odd Bits](solutions/leetcode/number_of_even_and_odd_bits.py)

[LeetCode 2595](https://leetcode.com/problems/number-of-even-and-odd-bits/)

You are given a positive integer `n`.

Let `even` denote the number of even indices in the binary representation of `n` (0-indexed) with value `1`.

Let `odd` denote the number of odd indices in the binary representation of `n` (0-indexed) with value `1`.

Return an integer array `answer` where `answer = [even, odd]`.

## [Palindrome Number](solutions/leetcode/palindrome_number.py)

[LeetCode 9](https://leetcode.com/problems/palindrome-number/)

Given an integer `x`, return `true` if `x` is a palindrome, and false otherwise.

### [Plus One](solutions/leetcode/plus_one.py)

[Leet Code 66](https://leetcode.com/problems/plus-one/description/)

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of 
the integer. The digits are ordered from most significant to the least significant in left-to-right order. The large 
integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

### [Primes in Diagonal](solutions/leetcode/primes_in_diagonals.py)

[LeetCode 2614](https://leetcode.com/problems/prime-in-diagonal/description/)

You are given a 0-indexed two-dimensional integer array `nums`.

Return the largest **prime** number that lies on at least one of the **diagonals** of `nums`. In case, no prime is 
present on any of the diagonals, return 0.

### [Remove Stars from a String](solutions/leetcode/remove_stars_from_a_string.py)

[LeetCode 2390](https://leetcode.com/problems/removing-stars-from-a-string/description/)

You are given a string `s`, which contains stars `*`.

In one operation, you can:

- Choose a star in `s`.
- Remove the closest **non-star** character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

### [Roman to Integer](solutions/leetcode/roman_to_int.py)

[LeetCode 13](https://leetcode.com/problems/roman-to-integer/description/)

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

### [Split With Minimum Sum](solutions/leetcode/split_with_minimum_sum.py)

[LeetCode 2578](https://leetcode.com/problems/split-with-minimum-sum/)

Given a positive integer `num`, split it into two non-negative integers `num1` and `num2` such that:
- The concatenation of `num1` and `num2` is a permutation of `num`.
- `num1` and `num2` can contain leading zeros.

Return the **minimum** possible sum of `num1` and `num2`

### [Two Sum](solutions/leetcode/two_sum.py)

[Twos Sum](https://leetcode.com/problems/two-sum/) is a problem in where you are given an array of integers `nums` and 
an integer `target`, then return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

### [Valid Parentheses](solutions/leetcode/valid_parentheses.py)

[LeetCode 20](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Codewars

## [Your order, please](solutions/codewars/your_order_please.py)

[Codewars Link](https://www.codewars.com/kata/55c45be3b2079eccff00010f)

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

**Example**

```text
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```
