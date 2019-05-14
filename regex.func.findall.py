import re

#Return a list containing every occurrence of "ai":

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
