class ValidParentheses:
    # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    # An input string is valid if:

    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.

    # Example 1:

    # Input: s = "()"
    # Output: true
    # Example 2:

    # Input: s = "()[]{}"
    # Output: true
    # Example 3:

    # Input: s = "(]"
    # Output: false

    # Notes before starting:
    # Iterate over the string
    # Check the current string and see if it's an open or closed bracket.
    # Opening brackets should be kept on a stack
    #   If it's an open bracket it's always allowed.
    #   append to stack
    # If it's a closed bracket it has to match the prior opening bracket.
    #  Check value at top of stack against valid pairings to make sure that validPairings[newest value on closed stack] = current

    # Runtime: 47 ms, faster than 41.93% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 13.8 MB, less than 97.97% of Python3 online submissions for Valid Parentheses.

    validPairings = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    openers = set(validPairings.keys())
    closers = set(validPairings.values())

    def isValid(self, s: str) -> bool:
        openStack = []
        for i in range(len(s)):
            current = s[i]
            # Append all open chars to openStack
            if current in self.openers:
                openStack.append(current)
                continue

            # We know we are a closing bracket
            # If we are a closing bracket without any openers then fail
            if not openStack:
                return False

            if self.validPairings[openStack[-1]] != current:
                return False

            # Was valid so pop off end of stack
            openStack.pop()

        return not openStack
