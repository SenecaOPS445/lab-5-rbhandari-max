#!/usr/bin/env python3
# Author ID: rbhandari17@myseneca.ca

def add(number1, number2):
    try:
        # Attempt to add the numbers after converting them to integers
        return int(number1) + int(number2)
    except ValueError:
        # If there's a ValueError (e.g., can't convert to int), return a user-friendly error message
        return 'error: could not add numbers'

def read_file(filename):
    try:
        # Try to open the file and read its lines
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        # If the file doesn't exist, we don't have permission, or it's a directory instead of a file, return an error message
        return 'error: could not read file'

if __name__ == '__main__':
    # Test cases for add function
    print(add(10, 5))                      # works (prints 15)
    print(add('10', 5))                    # works (prints 15)
    print(add('abc', 5))                   # exception (prints 'error: could not add numbers')
    print(add('hello', 'world'))           # exception (prints 'error: could not add numbers')

    # Test cases for read_file function
    print(read_file('seneca2.txt'))       # works (returns list of lines if file exists)
    print(read_file('file10000.txt'))     # exception (prints 'error: could not read file')
