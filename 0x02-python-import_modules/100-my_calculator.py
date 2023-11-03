#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    nbr_args = len(sys.argv)
    if nbr_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        valid_operators = {'+', '-', '*', '/'}
        if operator not in valid_operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if operator == "+":
                result = add(a, b)
            elif operator == "-":
                result = sub(a, b)
            elif operator == "*":
                result = mul(a, b)
            else:
                result = div(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
