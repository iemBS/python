import re

#Replace all white-space characters with the digit "9":

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
