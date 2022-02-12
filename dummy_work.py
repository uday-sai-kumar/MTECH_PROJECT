import pandas as pd
import numpy as np
d = [1, 2]
ser = pd.Series(data=d,copy=False)
ser.iloc[0]=100
print(d)
print('_______')
print(ser)