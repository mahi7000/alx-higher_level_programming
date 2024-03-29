#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    count = len(sys.argv) - 1
    if (count != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if (sys.argv[2] != "+" and sys.argv[2] != "-" and
            sys.argv[2] != "*" and sys.argv[2] != "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    operations = {"+": add, "-": sub, "*": mul, "/": div}
    print("{} {} {} = {}".format(a, op, b, operations[op](a, b)))
