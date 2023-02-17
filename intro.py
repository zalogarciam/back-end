def sum(a, b): return int(a) + int(b)
def subs(a, b): return int(a) - int(b)
def mult(a, b): return int(a) * int(b)
def div(a, b): return int(a) / int(b)
def calc(opt, a, b):
    if opt == '+': return sum(a, b)
    elif opt == '-': return subs(a, b)
    elif opt == '*': return mult(a, b)
    elif opt == '/': return div(a, b)
    else: return "wrong operation"

a = input('a: ')
b = input('b: ')
opt = input('operation: ')
print(str(calc(opt, a, b)))

