import Calc2D as C2
import sympy as sp

def main():
    x, y = sp.symbols("x y")
    func = sp.sin(x) + y
    print(isinstance(func, sp.core.expr.Expr))


if __name__ == "__main__":
    main()