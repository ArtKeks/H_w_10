import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})

for value in data['whoAmI'].unique():
    data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)

data.head()

