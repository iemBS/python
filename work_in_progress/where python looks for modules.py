Python has a simple algorithm for finding a module with a given name, such as a_module. It looks for a file called a_module.py in the directories listed in the variable sys.path.


>>> import sys
>>> type(sys.path)
<class 'list'>
>>> for path in sys.path:
...     print(path)
