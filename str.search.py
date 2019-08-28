line = "123|*abcdef*|456|*hijklm*|789"

print(line[line.find("|*")+2:line.find("*|")])

