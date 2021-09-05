import Calc2D as C2
import sympy as sp

def main():
    x, y = sp.symbols("x y")
    func = sp.sin(x)
    print(type(func))


if __name__ == "__main__":
    main()