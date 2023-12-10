from sqlalchemy import create_engine
from yaml import load, SafeLoader
import pandas as pd

class RDSDatabaseConnector:
    '''
    This class is used to represent a connection to an RDS database.
    
    Attributes:
        creds_filepath (str): the filepath to the credentials required to connect to the RDS database.
        table (str): the name of the table that is to be extracted from the cloud.
        data_filepath (str): the filepath that the extracted dataset should be saved to.
        format_creds (str): the formatted credentials that will be used as input for the sqlalchemy engine.
        engine (sqlalchemy.engine.base.Engine): the engine that will be used to connect to the RDS database.
        pandas_df (pandas.core.frame.DataFrame): the dataset extracted from the cloud.
    '''
    def __init__(self, creds_filepath, table, data_filepath):
        '''
        See help(RDSDatabaseConnector) for accurate signature.
        '''
        self.creds_filepath = creds_filepath
        self.table = table
        self.data_filepath = data_filepath
        self.format_creds = self.get_db_credentials()
        self.engine = self.initialise_engine()
        self.pandas_df = self.extract_from_cloud()

    def get_db_credentials(self):
        '''
        This function gets the credentials for connecting to the RDS database and formats them
        to be used as input for the sqlalchemy engine.
        '''
        with open(self.creds_filepath) as f:
            creds = load(f, Loader=SafeLoader)
            format_creds = (f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}"
                            f"@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
            return format_creds

    def initialise_engine(self):
        '''
        This function initialises the sqlalchemy engine.
        '''
        engine = create_engine(self.format_creds)
        engine.connect()
        return engine

    def extract_from_cloud(self):
        '''
        This function extracts the dataset from the cloud.
        '''
        pandas_df = pd.read_sql_table(self.table, self.engine)
        return pandas_df

    def save_to_csv(self):
        '''
        This function saves the pandas DataFrame in a .csv format.
        '''
        self.pandas_df.to_csv(self.data_filepath)

    def load_from_csv(self):
        '''
        This function loads the .csv dataset and prints the first 5 rows and the shape.
        '''
        data = pd.read_csv(self.data_filepath)
        print(data.head())
        print(data.shape)
        return data

if __name__ == '__main__':
    loans = RDSDatabaseConnector('credentials.yaml', 'loan_payments', 'loan_payments.csv')
    loans.get_db_credentials()
    loans.initialise_engine()
    loans.extract_from_cloud()
    loans.save_to_csv()
    loans.load_from_csv()
