"""

Main program to run the requirements for Project 4
Garrett Matthews

"""

from stack import Stack


def precedence(operator):
    """Returns the precedence of an operator"""
    if operator not in ['(', ')', '[', ']', '{', '}', '*', '/', '%', '+', '-']:
        raise ValueError("Error " + operator + " is not currently a supported operator")
    if operator in [')', ']', '}']:
        return 3
    if operator in ['*', '/', '%']:
        return 2
    if operator in['+', '-']:
        return 1
    if operator in['(', '[', '{']:
        return 0


def in2post(exp):
    """Evaluates an infix expression and converts it and returns it as a postfix express"""
    if not isinstance(exp, str):
        raise ValueError("Error - submitted expressions must be a string")
    operator = ['(', ')', '[', ']', '{', '}', '*', '/', '%', '+', '-']
    postfix = ''
    stack = Stack()
    print("Length: " + str(len(exp)))
    count = 0
    for i in exp:
        print(count)
        if i not in operator:
            postfix += i
        else:
            if stack.size() == 0:
                stack.push(i)
            elif i == ')':
                operator = ''
                while operator is not '(' and stack.size() != 0:
                    operator = stack.pop()
                    if operator is not '(':
                        postfix += operator
            elif i == ']':
                operator = ''
                while operator is not '[' and stack.size() != 0:
                    operator = stack.pop()
                    if operator is not '[':
                        postfix += operator
            elif i == '}':
                operator = ''
                while operator is not '{' and stack.size() != 0:
                    operator = stack.pop()
                    if operator is not '{':
                        postfix += operator
            elif precedence(i) > precedence(stack.peek()) or precedence(i) == 0:
                stack.push(i)
            else:
                operator = ')'
                while precedence(i) < precedence(operator) and stack.size() != 0:
                    operator = stack.pop()
                    postfix += operator
                stack.push(i)
        if (count == len(exp) - 1) and stack.size() > 0:
            while stack.size() > 0:
                operator = stack.pop()
                postfix += operator
        count += 1
    return postfix


def eval_postfix(exp):
    """Evaluates a postfix expression"""
    if not isinstance(exp, str):
        raise ValueError("Error- must submit a valid postfix string")
    numbers = []
    for i in range(10):
        numbers.append(str(i))
    operator = ['*', '/', '%', '+', '-']
    stack = Stack()
    for i in exp:
        if i in numbers:
            stack.push(float(i))
        elif i in operator:
            if stack.size() > 1:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '*':
                    ans = float(op1) * float(op2)
                    stack.push(ans)
                elif i == '/':
                    ans = float(op1) / float(op2)
                    stack.push(ans)
                elif i == '%':
                    ans = float(op1) % float(op2)
                    stack.push(ans)
                elif i == '+':
                    ans = float(op1) + float(op2)
                    stack.push(ans)
                elif i == '-':
                    ans = float(op1) - float(op2)
                    stack.push(ans)
            else:
                raise SyntaxError("Not a valid postfix expression")
    answer = stack.pop()
    return answer


def main():
    """Main function to run the program"""
    output = ''
    with open("data.txt", 'r') as data:
        for line in data:
            output += '\n' + "Infix: " + line
            postfix = in2post(line)
            output += "Postfix: " + postfix
            answer = eval_postfix(postfix)
            output += "Answer: " + answer + '\n'
    print(output)


if __name__ == "__main__":
    main()
