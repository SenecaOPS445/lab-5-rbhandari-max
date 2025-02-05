#!/usr/bin/env python3
# Author ID: rbhandari17@myseneca.ca
# lab5b.py

# Function to read file contents as a string
def read_file_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()

# Function to append a string to the file
def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

# Function to write a list of lines to a file
def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

# Function to read file contents into a list, each line as a separate element
def read_file_list(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]  # Remove newline characters

# Function to copy file contents to another file, adding line numbers
def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as f:
        lines = f.readlines()
    
    with open(file_name_write, 'w') as f:
        for i, line in enumerate(lines, start=1):
            f.write(f"{i}:{line.strip()}\n")  # Add line number at the beginning of each line

# Main script to execute functions
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    # Append string to file1 and print its contents
    append_file_string(file1, string1)
    print(read_file_string(file1))

    # Write list of lines to file2 and print its contents
    write_file_list(file2, list1)
    print(read_file_string(file2))

    # Copy file2 to file3 with line numbers and print file3 contents
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

