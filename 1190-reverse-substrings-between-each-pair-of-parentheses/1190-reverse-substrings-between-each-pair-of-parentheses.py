class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            portion = []
            if char==")":
                while(stack[-1]!="("):
                    portion.append(stack.pop())
                stack.pop()
                stack.extend(portion)
            else:
                stack.append(char)
        return "".join(stack)