def is_balanced(brackets):
    opens=["(","[","{"]
    closed=[")","]","}"]
    stack1=[]
    
    for char in brackets:
        if char in opens:
            stack1.append(char)
        else:
            if not stack1:
                return "NO"
            top = stack1.pop()
            if (top == "(" and char != ")") or \
               (top == "[" and char != "]") or \
               (top == "{" and char != "}"):
                return "NO"
    return "YES" if not stack1 else "NO"

print(is_balanced("(({{[[]]}}))"))    