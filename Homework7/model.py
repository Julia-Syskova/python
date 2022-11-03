import view

string: str = ''
result: int  = 0

operations = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: (int(x) / int(y)) if int(y) != 0 else view.division_be_zero(),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}

def line(string: str):
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ')
    list = string.split()
    return list