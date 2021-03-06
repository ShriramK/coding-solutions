# http://www.spoj.pl/problems/ONP/
import sys


def transform_expression(algebraic_expression):
    output = ""
    li = []
    for i in algebraic_expression:
        if str.isalpha(i):
            output += i
        elif i == '(':
            li.append(i)
        elif i == ')':
            temp = li.pop()
            while temp != '(':
                output += temp
                temp = li.pop()
        else:
            if li[len(li) - 1] == '(' or \
               det_priority(i) < det_priority(li[len(li) - 1]):
                li.append(i)
            else:
                output += li.pop()
                li.append(i)
    return output


def det_priority(operator_param):
    val = -1
    operator_values = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        '^': 4,
        '(': 5,
        }
    val = operator_values[operator_param]
    return val


num_of_expressions = int(raw_input())
for i in range(num_of_expressions):
    print transform_expression(raw_input())
