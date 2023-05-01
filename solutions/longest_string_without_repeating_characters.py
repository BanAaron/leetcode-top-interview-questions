class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if len(string) == 1:
            return 1

        # a set is basically a list that can only contain unique values
        seen = set()
        longest = 0
        substring = ""

        # loop through our string
        for i, char in enumerate(string):
            # for each character in the string loop through the string again starting from the current character
            # position
            for char2 in string[i:]:
                # if we haven't seen the character, we store it in seen and append to our substring
                if char2 not in seen:
                    seen.add(char2)
                    substring += char2
                # once we find a character we have already seen the substring won't be unique
                elif char2 in seen:
                    # store whatever is longer, the substring we're working on or the one we have stored
                    longest = max(longest, len(substring))
                    # cleanup our storage for the next loop
                    seen.clear()
                    substring = ""
                    # we can break at this point because there is no reason to check any further characters
                    break
        return longest
