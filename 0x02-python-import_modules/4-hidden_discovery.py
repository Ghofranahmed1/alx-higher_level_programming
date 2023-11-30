#!/usr/bin/python3
import hidden_4

names = dir(hidden_4)
names = [name for name in names if not name.startswith('__')]
names.sort()
for name in names:
    print(name)

if __name__ == "__main__":
    pass
