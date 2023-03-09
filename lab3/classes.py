#1
# Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case.

class my_class:
    def __init__(self):
        self.str = ""

    def getString(self):
         self.str = input()

    def printString(self):
        print(self.str.upper())
        
cc = my_class()
cc.getString()
cc.printString()


