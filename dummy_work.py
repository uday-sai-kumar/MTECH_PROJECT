import pandas as pd
import pyarrow.feather as feather

# rows= [1,2,3]
# columns = ['a','b','c']
# data= [[1, 2, 3], [4, 5, 0], [5, 6, 7]]
# data_frame = pd.DataFrame(columns=columns, index=rows)
# data_frame.fillna(0, inplace=True)
# data_frame.loc[1,'a'] = 4344
# feather.write_feather(data_frame,"/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/feather_file/hello")
df = feather.read_feather("/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/feather_file/hello")
print(df)