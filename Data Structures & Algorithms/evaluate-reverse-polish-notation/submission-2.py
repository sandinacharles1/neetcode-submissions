class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        I'm thinking we can put the symbols in a stack, and for every number, we perform the action
        So, loop through tokens once, get all the symbols
        Loop again, if theres a number, perform the symbol to the next number after it. check if integer
        '''

        '''New Logic:We can just loop over inn one place in a stack. Hear me out, we add the first two values to the stack, then we pop them and perform the operationn on it, thenn we get our new value PLUS the evaluated value, then we perform the operation on it. It's kind of intuitive, my problem earlier was figuringn out how to add / multiply to our pre-evaluated value,, but trrating it like a stack number and keeping thhe stack short because of the fact we'd have to pop it is smart

        Knowledge: Postfix, understanding the operators apply to the two most recent operands. this most recent knowledge is why we use a stack. our most recent number and the one before that (which would probably be pre-evaluated)
        '''
        #1. Identify the operators and intiialize stack with values from least recent to most recent
        stack = [] 
        operators = {"+","-","*","/"}
        
        #2. Loop through the list
        for i in tokens: #Loop through the ITEMS in a list, if u use range then u loop w numbers
            #3.5. Check if it's an operator. If it is, then perform algorithmic actions. You pop the two most recent numbers then add / multiply, or get the previous value (since stack is LIFO we want the first one to be the one we subtract or divide from)
            if i in operators: #If it's a operator
                operator = i
                match operator:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "-":
                        #stack.append(stack.pop() - stack.pop()). wait this doesnt work. we subtract the SECOND-to most recent (so the second one popped to the most recent)
                        num1, num2 = stack.pop(), stack.pop()
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(stack.pop() * stack.pop())
                    case "/":
                        num1, num2 = stack.pop(), stack.pop()
                        stack.append(int(num2 / num1))
            else: #3.5 append all numbers to stack
                stack.append(int(i))

        return stack[0]  #4. Return the last remaining number after all the math


    