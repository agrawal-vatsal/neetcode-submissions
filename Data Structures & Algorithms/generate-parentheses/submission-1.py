class Solution:
    ans = []

    def gen(self, op, close, string):
        if op == 0 and close == 0:
            self.ans.append(string)
            return

        if op:
            self.gen(op - 1, close, string + "(")

        if close > op:
            self.gen(op, close - 1, string + ")")
        

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.gen(n, n, "")
        return self.ans