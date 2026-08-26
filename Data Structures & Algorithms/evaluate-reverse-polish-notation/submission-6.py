class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                match token:
                    case "+":
                        result = first_num + second_num
                        stack.append(result)
                    case "-":
                        result = first_num - second_num
                        stack.append(result)
                    case "*":
                        result = first_num * second_num
                        stack.append(result)
                    case "/":
                        result = int(first_num / second_num)
                        stack.append(result)
                
                    
        return stack[0]