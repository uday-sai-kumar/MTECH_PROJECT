import pandas as pd


class CreateDataFrame:
    @classmethod
    def create_data_frame(cls, _data):
        _data_frame = pd.DataFrame(_data)
        return _data_frame

