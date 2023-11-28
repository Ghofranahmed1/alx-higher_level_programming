#!/usr/bin/python3
for i in range(00, 100):
    print("{}".format(str(i).zfill(2)), end="")
    if (i != 99):
        print(", ", end="")
