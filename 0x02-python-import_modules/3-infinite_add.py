#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    list_argv = sys.argv
    result = 0

    for i in list_argv[1:]:
        i = int(i)
        result = int(result + i)
    print(result)
