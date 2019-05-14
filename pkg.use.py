# PIP is a package manager for Python packages, or modules if you like.
# If you have Python version 3.4 or later, PIP is included by default.
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.
