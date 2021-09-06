#DESMOS: https://www.desmos.com/calculator/dzriauachx

import sympy as sp
from enum import Enum
from typing import Tuple

#an enum to select solid type for solids of revolution
class SolidType(Enum):
    CIRCLE = 0
    SQUARE = 1
    ISOTRI = 2 #isosceles triangle, or 1/2 of a square

#a set of type definitions for compressing and decompressing power functions
constantSeries = list[int]
partiallyCompressedPowerFunction = Tuple[sp.core.expr.Expr, constantSeries]

#return a taylor series expansion to an arbitrary number of terms
def getTaylorSeriesExpansion(func: sp.core.expr.Expr, terms: int) -> sp.core.expr.Expr:
    pass

#takes a single function and it's bounds, and returns the volume of a solid of revolution about the x axis based on the solidtype enum
def singleFunctionVolOfRev(func: sp.core.expr.Expr, solidtype: SolidType, a: int, b: int) -> sp.Float :
    pass

#takes a single power function and compresses it into a series of constants
def compressPowerFunction(func: sp.core.expr.Expr) -> constantSeries:
    pass

#takes a constant series and decompresses it into a power function
def decompressConstantSeries(series: constantSeries) -> sp.core.expr.Expr:
    pass

#TODO: Write the taylor series function
#TODO: Write the singleFunctionVolOfRev function
#TODO: Begin a multivariable calc file
#TODO: Write the compression/decompression pair