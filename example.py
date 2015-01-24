__author__ = 'Noah Peeters'

from mathexpressions import math

parser = math.Parser()

parser.parse_function('3+4')
parser.improve_function()
print(parser.calc_function())