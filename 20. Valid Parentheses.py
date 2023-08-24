class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack
        stack = []

        # Iterate through each char in string
        for char in s:
            # If char is a closing bracket, check if top of stack is an open bracket of the same type, if not, return False
            if( char == ')' or char == '}' or char == ']' ):
                # Checks if stack is empty
                if (len(stack) == 0):
                    return False

                # Checks if the top is stack is a matching bracket
                topChar = stack.pop()
                if ( char == ')' and topChar != '(' ):
                    return False
                elif ( char == '}' and topChar != '{' ):
                    return False
                elif ( char == ']' and topChar != '[' ):
                    return False
                    
            # If char is not closing bracket, assume open brack and push to stack
            else:
                stack.append(char)

        # If stack is empty, then Parentheses were valid.
        return (len(stack) == 0)