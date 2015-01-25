__author__ = 'Noah Peeters'

import time

import mathexpressions


# first create a parser object
parser = mathexpressions.Parser()

# add all variables; the value will not be used while parsing and improving
# variable names can be as long as you want
# variable names are case sensitive
# variable names can not start with a number or strings that are used as function name, constant name or operators
# not allowed: '+xg' '4tb' 'sine' 'x h'
# allowed: 'x' 'helloiamavariable' 'hello43'
# parser.add_var('x', 3)

# parse a function
parser.edit_const({'y': [3, 'x'], 'z': [7, 'z']})
parser.parse_function('x^y+z')

parser.set_var({'x': [3, 'x']})

# at this point the value of variables are used
# print('value of x: ' + str(parser.get_var('x')))
print(parser.calc_function())


# edit the value of a variable
parser.set_var({'x': [4, 'x']})
# it is possible to calculate the same function without parsing it again
print(parser.calc_function())

print('')

# it is possible to override the value of a const, even if that dose not make sense
parser.set_const({'pi': [4, '\pi']})
parser.parse_function('pi')
print(parser.calc_function())

# and removing them again
parser.set_const({})
parser.parse_function('pi')
print(parser.calc_function())

print('')

# if you want to calculate the same function multiple times, it makes sense to improve it
parser.parse_function('1+2*(x)^(2+pi)')
start = time.time()
for i in range(10):
    parser.set_var({'x': [i, 'x']})
    parser.calc_function()
print('time without improving: ' + str(time.time() - start))

parser.parse_function('1+2*(x)^(2+pi)')
parser.improve_function()  # function = '1+2*x^5.141592653589793'
start = time.time()
for i in range(10):
    parser.set_var({'x': [i, 'x']})
    parser.calc_function()
print('time with    improving: ' + str(time.time() - start))

print('')

# export the function as latex
parser.parse_function('sin(x)^2')
parser.improve_function()
print('Latex: ' + parser.get_latex() + '=' + str(parser.calc_function()))
parser.parse_function('x^2=4')
print('Latex: ' + parser.get_latex())
parser.set_var({'x': [1, 'x']})
print(parser.compare_function())