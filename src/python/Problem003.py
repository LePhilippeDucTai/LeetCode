# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.  # noqa: E501

# Gives the list of all of the substrings that form the string s of given size

import python.timing as timing


def _substrings(s: str, of_size: int) -> set:
    def length_of_uniques(st):
        return len("".join(set(st)))

    def loop(acc: set, s: str) -> set:
        length = len(s)
        if length < of_size or length == 0:
            return acc
        acc.add(length_of_uniques(s[:of_size]))
        return loop(acc, s[1:])

    return loop(set(), s)


class Solution:
    @timing.time_it
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)

        def max_set(my_set):
            return max(my_set) if bool(my_set) else 0

        def loop(length):
            x = max_set(_substrings(s, length))
            return length if x == length else loop(x)

        return loop(size)


if __name__ == "__main__":
    s = (
        "iqgpabaalqgovakobfymyjzbbuxmihdqalfanhaayiovkamnikagtzhvvhjdqnvqydsnkuqkcegpfucpeevaffxcoghevdvw"
    )
    # s = "bbbbb"
    # s = ""
    obj = Solution()
    print(obj.lengthOfLongestSubstring(s))
