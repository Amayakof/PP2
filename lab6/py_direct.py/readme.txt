OS module - provides functions for interacting with the operating system. 
OS comes under Python’s standard utility modules.

File hadling
The open() function takes two parameters; filename, and mode.
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - text mode

"b" - binary mode

To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt", "rt")

functions:
- open()
- read() -> also can specify how many characters to read: file.read(5)
- readline() -> returns one line
- close() -> on't forget to close the file when you finish working
