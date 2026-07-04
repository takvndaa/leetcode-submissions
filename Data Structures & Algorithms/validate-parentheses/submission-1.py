class Solution:
    def isValid(self, s: str) -> bool:
        # input str s of parentheses
        # output bool
        # all open parencthesis must be closed
        # in correct order
        # in matching pairs
        # search and replace pairs 
        # quadratic time and linear space
        # use stack and hashmap

        matches = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        stack = []

        for c in s:
            if c in matches.values():
                stack.append(c)
            else:
                if stack and stack[-1] == matches[c]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
        