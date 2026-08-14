'''
    0.Return the sum after alll the operations have been process
    1. 
        [] -> 0
        [1] -> 1
        
        [1,D,2, C, 3]
        1: stack = [1]
        D; [1,1*2]
        2: [1,2,2]
        C: [1,2]
        3: [1,2,3]
        returns 6
    2 & 3. O(n) time and O(n) space
        check if the operations are empty: if they are return 0

        -create a stack 
        for each operation:
            if its just a number : store the number in the stack
            if its a + symbol: pull out the two previous numbers add them and then add that as a new number to our stack 
            if its the letter D: take previous number and multiply it by 2
            if its the letter C: remove the previous number from the stack
        
        return the sum of all the numbers in the list 
    
'''


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        if not operations: return 0
        stack = []
        for val in operations:
            if val == '+':
                val1 = stack[len(stack) - 1]
                val2 = stack[len(stack) - 2]
                stack.append(val1 + val2)
            elif val == 'D': 
                val1 = stack[len(stack) - 1]
                stack.append(val1 * 2)
            elif val == 'C': stack.pop()
            else: stack.append(int(val))
        
        return sum(stack)

        
        # return the sum of all the numbers in the list 
       
    

        