import pandas as pd

class DataTransform:
    '''
    This class is used to represent a set of transformations to a dataset.
    
    Attributes:
        df (pandas.core.frame.DataFrame): the dataset to be transformed.
    '''
    def __init__(self, df):
        '''
        See help(DataTransform) for accurate signature.
        '''
        self.df = df

    def to_category(self, column):
        '''
        This function converts a column to a categorical format.
        
        Args:
            column (pandas.core.series.Series): the column to be converted.
        '''
        self.df[column] = self.df[column].astype('category')

    def to_datetime(self, column):
        '''
        This function converts a column to a datetime format.
        
        Args:
            column (pandas.core.series.Series): the column to be converted.
        '''
        self.df[column]  = pd.to_datetime(self.df[column])