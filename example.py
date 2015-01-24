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
parser.add_var('x', 3)

# parse a function
parser.parse_function('x^2')

# at this point the value of variables are used
print('value of x: ' + str(parser.get_var('x')))
print(parser.calc_function())


# edit the value of a variable
parser.edit_var('x', 2)
print('')
print('value of x: ' + str(parser.get_var('x')))
# it is possible to calculate the same function without parsing it again
print(parser.calc_function())

print('')

# it is possible to override the value of a const, even if that dose not make sense
parser.add_var('pi', 3)
parser.parse_function('pi')
print(parser.calc_function())

# and removing them again
parser.remove_var('pi')
parser.parse_function('pi')
print(parser.calc_function())

print('')

# if you want to calculate the same function multiple times, it makes sense to improve it
parser.parse_function('1+2*(x)^(2+pi)')
start = time.time()
for i in range(4):
    parser.edit_var('x', i)
    parser.calc_function()
print('time without improving: ' + str(time.time() - start))

parser.parse_function('1+2*(x)^(2+pi)')
parser.improve_function()  # function = '1+2*x^5.141592653589793'
start = time.time()
for i in range(4):
    parser.edit_var('x', i)
    parser.calc_function()
print('time with    improving: ' + str(time.time() - start))

print('')

# export the function as latex
parser.parse_function('sin(x)^2')
parser.improve_function()
print('Latex: ' + parser.get_latex() + '=' + str(parser.calc_function()))