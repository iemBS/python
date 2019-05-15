# Variable Scope: Most variables in Python are local in scope to their own function or class. For instance if you define a = 1 within a function, then a will be available within that entire function but will be undefined in the main program that calls the function. Variables defined within the main program are accessible to the main program but not within functions called by the main program.
# Global Variables: Global variables, however, can be declared with the global keyword.
a = 1
b = 2
def Sum():
   global a, b
   b = a + b
Sum()
print(b)
-> 3 
