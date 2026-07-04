class Solution:
    def isValid(self, s: str) -> bool:
        # input : str s of parentheses
        # bool
        # valid if all open brackets are closed
        # brackets are matched
        # brackets are paired in order

        stack = []
        matches = {']' : '[', '}' : '{', ')':'('}

        for c in s:
            if c in matches.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != matches[c]:
                    return False

        return len(stack) == 0
            
        