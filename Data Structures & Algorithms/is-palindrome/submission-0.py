class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # c = "".join(s)
        return c == c[::-1]


        