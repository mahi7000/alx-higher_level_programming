#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    add = 0
    for i in range(1, count):
        add += int(sys.argv[i])
    print(add)
