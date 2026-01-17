"""
In this lesson, we learned how to read files in Python, which is an essential skill for working with stored data. 
Python provides three main methods for reading files: read, readline, and readlines. 
The read method allows you to grab the entire content of a file as a single string, while readline fetches just one line at a time. 
If you want to read all the lines at once and get them in a list format, you can use readlines.

Imagine you have a book. If you want to read the whole book, you would use the read method. 
If you only want to read the first page, you would use readline. 
And if you want to gather all the pages into a stack to look through them later, you would use readlines. 
This way, you can choose how much of the file you want to read based on your needs!


"""


# Reading the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("Reading the entire file:")
    print(content)
# Reading one line at a time
with open("example.txt", "r") as file:
    print("Reading one line at a time:")
    line = file.readline()
    while line:
        print(line, end='')  # end='' to avoid double newlines
        line = file.readline()
# Reading all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\nReading all lines into a list:")
    for line in lines:
        print(line, end='')  # end='' to avoid double newlines