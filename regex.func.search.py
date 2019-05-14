import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start()) 
