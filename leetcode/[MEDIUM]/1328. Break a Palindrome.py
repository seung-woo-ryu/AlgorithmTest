class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l = len(palindrome)
        if l == 1:
            return ""
        if l % 2 == 0:
            for i in range(l//2 + 1):
                if 'a' != palindrome[i]:
                    return palindrome[:i] + "a" + palindrome[i+1:]
            return palindrome[:l//2] + "b" + palindrome[l//2+1:]
        else:
            for i in range(l//2):
                if 'a' != palindrome[i]:
                    return palindrome[:i] + "a" + palindrome[i+1:]
            return palindrome[:-1] + "b"