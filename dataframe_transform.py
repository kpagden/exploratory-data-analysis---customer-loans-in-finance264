from scipy.special import boxcox1p
from scipy.stats import yeojohnson
import numpy as np
import pandas as pd

class DataFrameTransform:
    '''
    This class is used to represent a set of transformations to a pandas dataframe.
    
    Attributes:
        df (pandas.core.frame.DataFrame): the dataframe to be transformed.
    '''
    def __init__(self, df):
        '''
        See help(DataFrameTransform) for accurate signature.
        '''
        self.df = df

    def impute_mode(self, column):
        '''
        This function replaces missing values in a column with the mode.
        
        Args:
            column (pandas.core.series.Series): the column with missing values to be imputed.
        '''
        self.df[column].fillna(self.df[column].mode()[0], inplace=True)

    def impute_median(self, column):
        '''
        This function replaces missing values in a column with the median.
        
        Args:
            column (pandas.core.series.Series): the column with missing values to be imputed.
        '''
        self.df[column].fillna(self.df[column].median(), inplace=True)

    def log_transform(self, column):
        '''
        This function applies a log transformation to a skewed column.
        
        Args:
            column (pandas.core.series.Series): the column to be transformed.
        '''
        self.df[column] = self.df[column].map(lambda i: np.log(i) if i > 0 else 0)

    def boxcox_transform(self, column):
        '''
        This function applies a Box-Cox transformation to a skewed column.
        
        Args:
            column (pandas.core.series.Series): the column to be transformed.
        '''
        self.df[column] = self.df[column].map(lambda i: boxcox1p(i, 0.25))

    def yeojohnson_transform(self, column):
        '''
        This function applies a Yeo-Johnson transformation to a skewed column.
        
        Args:
            column (pandas.core.series.Series): the column to be transformed.
        '''
        self.df[column] = pd.Series(yeojohnson(self.df[column])[0])
        
    def remove_outliers(self, column):
        '''
        This function removes outliers from a column using the IQR.
        
        Args:
            column (pandas.core.series.Series): the column with outliers to be removed.
        '''
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        upper_limit = Q3 + 1.5 * IQR
        lower_limit = Q1 - 1.5 * IQR
        self.df = self.df[(self.df[column] > lower_limit) & (self.df[column] < upper_limit)]