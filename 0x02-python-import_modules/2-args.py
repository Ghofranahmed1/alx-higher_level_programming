#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    list_argv = sys.argv
    len_list = len(list_argv)

    if len_list == 1:
        print("0 arguments.")
    elif len_list == 2:
        print("1 argument:")
        print("1:", list_argv[1])
    else:
        print("{} arguments:".format(len_list-1))
        for i, value in enumerate(list_argv[1:]):
            print("{}: {}".format(i+1, value))
