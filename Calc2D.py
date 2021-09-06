#DESMOS: https://www.desmos.com/calculator/dzriauachx

import sympy as sp
from enum import Enum

class SolidType(Enum):
    CIRCLE = 0
    SQUARE = 1
    ISOTRI = 2 #isosceles triangle, or 1/2 of a square

#return a taylor series expansion to an arbitrary number of terms
def getTaylorSeriesExpansion(func: sp.core.expr.Expr, terms: int) -> sp.core.expr.Expr:
    pass

#takes a single function and it's bounds, and returns the volume of a solid of revolution about the x axis based on the solidtype enum
def singleFunctionVolOfRev(func: sp.core.expr.Expr, solidtype: SolidType, a: int, b: int) -> sp.Float :
    pass

#TODO: Write the taylor series function
#TODO: Write the singleFunctionVolOfRev function
#TODO: Begin a multivariable calc file