# How to use pandas.

import pandas as pd

data = ["Akshay", "kumar", 90, 23, 67]
ser = pd.Series(data)
print("data: ", data)
print("Series: \n", ser)


df = pd.DataFrame(data)
print("Data Frame: ", df)
