PyMathExpressions
-----------------

Python library for parsing and solving math expressions.

Simple example:

    >>> import mathexpressions
    >>> parser = mathexpressions.Parser()
    >>> parser.edit_var({'x':[3, 'x']})
    >>> parser.parse_function('x^2')
    >>> print(parser.calc_function())
    9
    >>> parser.edit_var({'x':[4, 'x']})
    >>> print(parser.calc_function())
    16
    
For advanced usage check out the documentation (http://pythonhosted.org/mathexpressions/).

Install the library with ``pip install mathexpressions``.
