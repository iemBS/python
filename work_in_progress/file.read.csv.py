import pandas as pd
df = pd.read_csv('name of the file.csv', sep=',')

In case you get the encoding error you can try:

import pandas as pd
df = pd.read_csv('name of the file.csv', sep=',', encoding='latin-1')
