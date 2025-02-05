#!/usr/bin/env python3
# Author ID: rbhandari17@myseneca.ca

def read_file_string(file_name):
    """
    Takes a file name as input and returns its entire contents as a string.
    """
    try:
        with open(file_name, 'r') as f:
            return f.read()  # Returns the entire content of the file as a string
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None

def read_file_list(file_name):
    """
    Takes a file name as input and returns its entire contents as a list of lines
    without the newline characters at the end of each line.
    """
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]  # Reads the lines and removes newline characters
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None

if __name__ == '__main__':
    file_name = 'data.txt'
    
    # Read the entire file as a string and print it
    print(read_file_string(file_name))
    
    # Read the file as a list and print it
    print(read_file_list(file_name))
