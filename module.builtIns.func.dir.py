# dir() returns properties, modules, and functions
# Without arguments, dir() returns the names you have defined currently
# dir() does not return the names of built-in functions and variables. 
# If you want to return built-in names, they are defined in the standard module "builtins".


import platform

x = dir(platform)
print(x)

y = dir(builtins)
print(y)

