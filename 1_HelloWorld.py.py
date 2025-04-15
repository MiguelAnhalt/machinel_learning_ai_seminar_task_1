######################################################################
#                                                                    #
# Task 1.1: Introduction to Python: Running hello world on VS Code   #
# Instructions:                                                      #
# • Your task is to print ‘Hello World from Your‐name’ in the        #
# Command line/ Terminal                                             #
# • A directory named home/username/Desktop/ML/Task1 needs to be     #
# created and inside that the 1_HelloWorld.py python file needs      #
# to be created                                                      #
#                                                                    #
#                                                                    #
# Author: Miguel Angel Lopez Mejia                                   #
######################################################################

class HelloWorld:
    def __init__(self,name):
        # Define the variables to be used in the class
        self.name = name 
        

    def print_hello(self):
        print(f"Hello World from {self.name}!") # Concatenates a string with the variable 'name'


def main():
    
    name = input('Introduce your name: ') # Ask to the user to introduce a name

    try:
        int(name) # Try to cast the name to be integer in order to identify if the user introduced a number instead of a string.
        print("The value must be string")
        return 0
    
    except Exception as e:    
        print_val = HelloWorld(name) # Create instance of the class HelloWorld

        print_val.print_hello() # Call the method that Concatenates a string with the variable 'name'
    

if __name__ == "__main__":
    main()