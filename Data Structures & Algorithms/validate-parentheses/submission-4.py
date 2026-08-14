

'''
    0.return true if a string is considered valid meaning opening and closing brackets, braces and parentheses, return false otherwise
    1.
        empty case -> returns true
        single case [] -> returns true
        [[[]]] -> returns true
        [{}) -> returns false 
    
    2.
        iterate through all of the symbols:
            check if the current symbol is an oppening brace,bracket or peren and add it to the stack:
            otherwise if its something else: 
            pop the last element and check if the current closing symbol has a corresponding opening symbol if it does continue if it doesnt return false
    
    3.
        check if the list is empty if it is return true

        for ever symbol in the list:
            if it equals a parent, bracket or brace:
                push it into the stack
            else:
                pop the previous element from the stack and check if the current brace has its corresponding closing brace, and do this check for the other other 2 types. if no return false

        
        otherwise we are out of th eloop & return true 

'''


class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return False

        symbols = []
        for symbol in s:
            if symbol == '{' or symbol =='[' or symbol =='(': symbols.append(symbol)
            else:
                # check if the stack still contains elements
                if symbols:
                    previousSymbol = symbols.pop()
                    if  symbol == '}' and previousSymbol != '{': return False
                    elif symbol == ')' and previousSymbol != '(': return False
                    elif  symbol == ']' and previousSymbol != '[' : return False
                else: return False
        
        return len(symbols) == 0 

        