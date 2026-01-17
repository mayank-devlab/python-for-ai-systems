"""
Creating and Managing Files in Python: A Simple Explanation

Think of it like writing a note on a piece of paper. 
When you write something down, it stays there even after you leave the room. 
Similarly, when we create a file in Python, we can store information that will be available later, even if we turn off the computer.

To create a file, we use the open function. 
Imagine you have a box (the file) where you can put your notes (data). 
You can open this box in two ways: to write new notes (using "write" mode) or to add more notes without losing the old ones (using "append" mode). 

"""

# Creating and writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a simple file created using Python!\n")
    file.write("We can write multiple lines to this file.\n")



# Appending to the same file
with open("example.txt", "a") as file:
    file.write("This line is added later without deleting the previous content.\n")