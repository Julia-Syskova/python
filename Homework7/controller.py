import model
import view

def operat(list, i, oper):
    if list[i] == oper:
        list[i - 1] = model.operations.get(oper)(int(list[i - 1]), int(list[i + 1]))
        delete(list, i)
        return True
    return False

def delete(string, i):
    string.pop(i)
    string.pop(i)

def calculate(list: list):
    while len(list) > 1:
        if '*' in list or '/' in list:
            for i in range(len(list)):
                if operat(list, i, '*'): break
                if operat(list, i, '/'): break

        elif '+' in list or '-' in list:
            for i in range(len(list)):
                if operat(list, i, '+'): break
                if operat(list, i, '-'): break
    return list

def slice(expression: list):
    open_par, close_par = None, None
    for index, item in enumerate(expression):
        if item == "(": open_par = index
        elif item == ")": close_par = index
        if open_par != None and close_par != None:
            expression1 = expression[:open_par]
            expression2 = calculate(expression[open_par+1:close_par])
            expression3 = expression[close_par+1:]
            expression = []
            expression.extend(expression1)
            expression.extend(expression2)
            expression.extend(expression3)
            break
    return expression

def expression(expression: str):
    expression = model.line(expression)
    while len(expression) > 1:
        
        if ('(' in expression) and (')' in expression):
            expression = slice(expression)
        else:
            expression = calculate(expression)
    model.result = expression[0]
    view.result()