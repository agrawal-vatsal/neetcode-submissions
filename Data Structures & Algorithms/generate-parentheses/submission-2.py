class Solution:
    ans = []

    def gen(self, n, string, open_count, closed_count):
        if len(string) == 2 * n:
            self.ans.append(string)
            return

        if closed_count < open_count:
            self.gen(n, string + ")", open_count, closed_count + 1)

        if open_count < n:
            self.gen(n, string + "(", open_count + 1, closed_count)

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.gen(n, "", 0, 0)
        return self.ans
