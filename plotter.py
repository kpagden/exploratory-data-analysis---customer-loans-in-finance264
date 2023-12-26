import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd
import seaborn as sns

class Plotter:
    '''
    This class is used to represent a set of methods used for creating plots.
    
    Attributes:
        df (pandas.core.frame.DataFrame): the dataframe which plots will be created from.
    '''
    def __init__(self, df):
        '''
        See help(Plotter) for accurate signature.
        '''
        self.df = df

    def plot_nulls(self):
        '''
        This function creates a plot of null values for all columns in a dataframe.
        '''
        msno.matrix(self.df)

    def plot_distributions(self, cols):
        '''
        This function plots histograms for a given list of columns so that their distributions can be observed.
        
        Args:
            cols (list): A list of numeric columns to plot histograms for.
        '''
        f = pd.melt(self.df, value_vars=cols)
        g = sns.FacetGrid(f, col='variable', col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)

    def plot_outliers(self, cols):
        '''
        This function creates boxplots for a given list of columns so that outliers can be observed.
        
        Args:
            cols (list): A list of numeric columns to plot boxplots for.
        '''
        fig, axes = plt.subplots(nrows=8, ncols=3, figsize=(10,40))
        axes = axes.flatten()

        for idx, column in enumerate(cols):
            self.df.boxplot(column=column, ax=axes[idx])
            axes[idx].set_title(column)

        plt.tight_layout()
        plt.show()