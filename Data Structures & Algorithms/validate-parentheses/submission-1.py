class Solution:
    def isValid(self, s: str) -> bool:
        #Logic > The opening parenthesis follow a STACK format, where the last opening parenthesis are going to have the first opening parenthesisis because theyre in order > ({[open  close]}). 
        
        #match the closing parenthesis (after) to the open parenthesis earlier. so we can add all the opening to a list and pop the last in and see if it matches
        pair = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = [] #include all open parenthesis
        
        for i, value in enumerate(s):
            
            if value in pair.keys(): #If it's a closing parenthetic, pop it from the stack
                if not stack: #If theres a closing but no openeing
                    return False
                else:  #pop the match
                    open_pair  = stack.pop()
                    if open_pair != pair[value]:
                        return False
            else: #If it's a opening parenthetic, add to stacj
                stack.append(value)

        #Stack should be empty becasue everything is popped
        if not stack:
            return True
        else:
            return False
