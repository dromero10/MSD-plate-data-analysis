from string import ascii_uppercase
from general_functions import utility_functions as uf
import pandas as pd

class RawPlateData:
    '''
    This class is meant to represent the raw ecl data from the standard text 
    file output of MSD plate readers.
    '''
    # Define the indices for the header of the text file. They are constant 
    # for the MSD standard output
    HEADER_SKIP_ROWS = 1
    HEADER_N_ROWS = 21

    CLEANED_HEADER_FIELDS = [
        'filename',
        'run_name',
        'stack_id',
        'plate_num',
        'barcode1',
        'barcode2',
        'barcode3',
        'type',
        'wells_per_row',
        'wells_per_col',
        'spots_per_well',
        'det_param',
        'creation',
        'read_time',
        'version',
        'user',
        'comments',
        'serial_num',
        'model',
        'orient',
        'assays'
    ]

    # Rows to skip to get to the ECL data portion of the file. The key is spot number and the
    # value is nrows to skip when reading with pd.read_csv for auto-parsing columns. For example, for a 1-spot plate the 
    # microplate column labels begin on line 28 and the actual ECL counts begin on the next line (line 29)
    # i.e. skip index + 1 is the line where the ECL counts begin. 
    SKIP_INDICES_FOR_ECL = {
        1: 28,
        4: 31,
        7: 34,
        10: 36 
    }

    def __init__(self, path: str):
        '''
        constructor takes in a string of the path that is passed onto pd.read_csv
        '''
        self.path = path

        self.header_data = {key: None for key in self.CLEANED_HEADER_FIELDS}
        self.read_header_data()
        self.ecl_data = pd.DataFrame()
        self.read_ecl_data()

    def __str__(self) -> str:
        return f'{self.header_data["spots_per_well"]}-spot plate {self.header_data["barcode1"]} read on: {self.header_data["read_time"]}'

    def __repr__(self) -> str:
        return f'RawPlateData.RawPlateData(path={self.path})'

    def read_header_data(self):
        '''
        method to read in (most) of the header data from the text file. 
        '''
        header_import = pd.read_csv(
            self.path,
            sep = '\t',
            skiprows=self.HEADER_SKIP_ROWS,
            nrows=self.HEADER_N_ROWS,
            names=['col1','col2','col3']
        )
        header_import['col1'] = self.CLEANED_HEADER_FIELDS

        is_time_data = header_import['col1'].str.contains('creation|read_time')
        time_data = header_import.loc[is_time_data, ['col2','col3']]
        header_import = header_import.loc[~is_time_data,['col1','col2']]

        creation = uf.convert_to_datetime(time_data.iloc[0,0], time_data.iloc[0,1])
        read_time = uf.convert_to_datetime(time_data.iloc[1,0], time_data.iloc[1,1])
        self.header_data['creation'] = creation
        self.header_data['read_time'] = read_time

        for _, row in header_import.iterrows():   
            self.header_data[row['col1']] = row['col2']

        self.header_data['stack_id'] = float(self.header_data['stack_id'])
        self.header_data['plate_num'] = int(self.header_data['plate_num'])
        self.header_data['wells_per_row'] = int(self.header_data['wells_per_row'])
        self.header_data['wells_per_col'] = int(self.header_data['wells_per_col'])
        self.header_data['spots_per_well'] = int(self.header_data['spots_per_well'])

    def read_ecl_data(self):
        '''
        method to read the ecl data from the text file
        '''
        n_spots = self.header_data['spots_per_well']
        skip = self.SKIP_INDICES_FOR_ECL[n_spots]
        
        n_rows = self.header_data['wells_per_col']
        n_cols = self.header_data['wells_per_row']
        stop_index = n_spots * n_rows
        cols = [str(x) for x in range(1, n_cols+1)]
        cols.insert(0,'row')
        cols.append('unused_col')

        ecl_data = pd.read_csv(
            self.path,
            sep = "\t",
            names = cols,
            usecols = cols[:-1],
            skiprows = skip + 1,
            nrows = stop_index
        )

        ecl_data['row'] = RawPlateData._create_row_labels(n_rows=n_rows, n_spots=n_spots)
        ecl_data['spot'] = RawPlateData._create_spot_labels(n_rows=n_rows, n_spots=n_spots)

        self.ecl_data = ecl_data

    def melt_ecl_data(self) -> pd.DataFrame:
        '''
        unpivots ECL data to long format
        '''

        melted_df = self.ecl_data.melt(
            id_vars = ['row','spot'],
            value_vars = [str(x) for x in range(1,self.header_data['wells_per_row']+1)],
            var_name = 'col',
            value_name = 'ECL_signal'
        )
        melted_df['well'] = melted_df['row'] + melted_df['col']
        return melted_df

    def _create_row_labels(n_rows: int, n_spots: int) -> list:
        '''
        function that creates the row labels for the imported ecl data 
        '''
        letters_subset = ascii_uppercase[:n_rows]

        labels = []

        for letter in letters_subset:
            for _ in range(n_spots):
                labels.append(letter)

        return labels

    def _create_spot_labels(n_rows: int, n_spots: int) -> list:
        '''
        function that creates the spot labels for the imported ecl data
        '''
        labels = []

        for _ in range(n_rows):
            for spot in range(n_spots):
                labels.append(spot+1)
        return labels














    

