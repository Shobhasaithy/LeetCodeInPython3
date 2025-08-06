class Solution:
    def isValid(self, s: str) -> bool:
        def match(a,b):
            if(a=='(' and b == ')'):
                return True
            if(a=='{' and b == '}'):
                return True
            if(a=='[' and b == ']'):
                return True
            else:
                return False
        stack = []
        for i in range(len(s)):
            if(s[i] == '[' or s[i] == '{' or s[i] == '('):
                stack.append(s[i])
            if(s[i] == ']' or s[i] == '}' or s[i] == ')'):
                if(len(stack)==0):
                    return False
                temp = stack.pop()
                if(not match(temp,s[i])):
                    return False
        if(len(stack)==0):
            return True
        else:
            return False

  '''
  Simple balance parenthesis code
  Simple balanced parentheses checker:
- Uses a stack to track opening brackets.
- Matches each closing bracket with the top of the stack.
- Ensures proper nesting and pairing.
  '''
