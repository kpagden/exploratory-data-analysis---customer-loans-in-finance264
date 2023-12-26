import pandas as pd

class DataFrameInfo:
    '''
    This class represents a set of methods used to get information about a dataframe.
    
    Attributes:
        df (pandas.core.frame.DataFrame): the dataframe to retrieve information about.
    '''
    def __init__(self, df):
        '''
        See help(DataFrameInfo) for accurate signature.
        '''
        self.df = df

    def get_dtypes(self):
        '''
        This function returns the data types of columns in a dataframe.
        '''
        return self.df.info()

    def get_statistics(self):
        '''
        This function returns statistical values for numerical columns in a dataframe.
        '''
        return self.df.describe()

    def get_shape(self):
        '''
        This function returns the shape of a dataframe.
        '''
        return self.df.shape

    def count_distinct(self, column):
        '''
        This function returns the counts of distinct values in a column of a dataframe.
        
        Args:
            column (pandas.core.series.Series): the column to return the value counts for.
        '''
        return self.df[column].value_counts()

    def percentage_null_count(self):
        '''
        This function return the percentage of nulls for each column in a dataframe.
        '''
        return self.df.isna().mean() * 100

    