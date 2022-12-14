import sys
sys.path.insert(0, 'C:\\Users\\romero.daniel\\Documents\\Python_projects\\MSD_plate_data_analysis')

from numpy import nan
import unittest
import datetime
from classes import RawPlateData as rpd



class TestRawPlateData(unittest.TestCase):
    def setUp(self) -> None:
        self.plate_1spot = rpd.RawPlateData("C:\\Users\\romero.daniel\\Documents\\Python_projects\\MSD_plate_data_analysis\\example_docs\\1_spot_plate.txt")
        self.plate_4spot = rpd.RawPlateData("C:\\Users\\romero.daniel\\Documents\\Python_projects\\MSD_plate_data_analysis\\example_docs\\4_spot_plate.txt")
        self.plate_7spot = rpd.RawPlateData("C:\\Users\\romero.daniel\\Documents\\Python_projects\\MSD_plate_data_analysis\\example_docs\\7_spot_plate.txt")
        self.plate_10spot = rpd.RawPlateData("C:\\Users\\romero.daniel\\Documents\\Python_projects\\MSD_plate_data_analysis\\example_docs\\10_spot_plate.txt")
        self.plate_384_4spot = rpd.RawPlateData("C:\\Users\\romero.daniel\\Documents\\Python_projects\\MSD_plate_data_analysis\\example_docs\\384_well_4_spot_plate.txt")
        return super().setUp()
    def test_header_data(self):
        test_header_1spot = {
            'filename': 'C:\\ECLResults\\23M0DAVA63_2022-10-14-105624.txt',
            'run_name': 'MMP10-20221014',
            'stack_id': 0.1,
            'plate_num': 2,
            'barcode1': '<23M0DAVA63>',
            'barcode2': '<>',
            'barcode3': '<>',
            'type': '96 Small-Spot',
            'wells_per_row': 12,
            'wells_per_col': 8,
            'spots_per_well': 1,
            'det_param': 'Standard',
            'creation': datetime.datetime(2022, 10, 14, 10, 55, 15),
            'read_time': datetime.datetime(2022, 10, 14, 10, 56, 24),
            'version': 'MMPR 1.0.38',
            'user': 'rcohen@meso-scale.com',
            'comments': nan,
            'serial_num': '1200110328643',
            'model': 'HTS',
            'orient': 'Normal',
            'assays': nan
        }

        test_header_4spot = {
            'filename': 'C:\\ECLResults\\25K1CAT872_2022-10-14-125240.txt',
            'run_name': 'MMP3',
            'stack_id': 0.1,
            'plate_num': 2,
            'barcode1': '<25K1CAT872>',
            'barcode2': '<>',
            'barcode3': '<>',
            'type': '96 Multi-Spot 4',
            'wells_per_row': 12,
            'wells_per_col': 8,
            'spots_per_well': 4,
            'det_param': 'Standard',
            'creation': datetime.datetime(2022, 10, 14, 12, 51, 30),
            'read_time': datetime.datetime(2022, 10, 14, 12, 52, 40),
            'version': 'MMPR 1.0.38',
            'user': 'smisaghian@meso-scale.com',
            'comments': nan,
            'serial_num': '1200110328643',
            'model': 'HTS',
            'orient': 'Normal',
            'assays': ',,,'
        }

        test_header_7spot = {
            'filename': 'C:\\ECLResults\\29L2HA7065_2022-11-01-180443.txt',
            'run_name': '20221101-Angio and V-ProInflam',
            'stack_id': 0.1,
            'plate_num': 2,
            'barcode1': '<29L2HA7065>',
            'barcode2': '<>',
            'barcode3': '<>',
            'type': '96 Multi-Spot 7',
            'wells_per_row': 12,
            'wells_per_col': 8,
            'spots_per_well': 7,
            'det_param': 'Standard',
            'creation': datetime.datetime(2022, 11, 1, 18, 3, 33),
            'read_time': datetime.datetime(2022, 11, 1, 18, 4, 43),
            'version': 'MMPR 1.0.38',
            'user': 'rcohen@meso-scale.com',
            'comments': nan,
            'serial_num': '1200110328643',
            'model': 'HTS',
            'orient': 'Normal',
            'assays': ',,,,,,'
        }

        test_header_10spot = {
            'filename': 'C:\\ECLResults\\2BLFDA7243_2022-11-22-095753.txt',
            'run_name': 'Tau',
            'stack_id': 0.1,
            'plate_num': 1,
            'barcode1': '<2BLFDA7243>',
            'barcode2': '<>',
            'barcode3': '<>',
            'type': '96 Multi-Spot 10',
            'wells_per_row': 12,
            'wells_per_col': 8,
            'spots_per_well': 10,
            'det_param': 'Standard',
            'creation': datetime.datetime(2022, 11, 22, 9, 56, 18),
            'read_time': datetime.datetime(2022, 11, 22, 9, 57, 53),
            'version': 'MMPR 1.0.38',
            'user': 'msdservice',
            'comments': nan,
            'serial_num': '1300130118108',
            'model': 'QuickPlex',
            'orient': 'Normal',
            'assays': ',,,,,,,,,'
        }

        test_header_384_4spot = {
            'filename': 'C:\\ECLResults\\1LK01A7057_2020-06-24-130808.txt',
            'run_name': nan,
            'stack_id': 0.1,
            'plate_num': 1,
            'barcode1': '<1LK01A7057>',
            'barcode2': '<>',
            'barcode3': '<>',
            'type': '384 Multi-Spot 4',
            'wells_per_row': 24,
            'wells_per_col': 16,
            'spots_per_well': 4,
            'det_param': 'Standard',
            'creation': datetime.datetime(2020, 6, 24, 13, 6, 38),
            'read_time': datetime.datetime(2020, 6, 24, 13, 8, 8),
            'version': 'MMPR 1.0.27',
            'user': 'nsammons@meso-scale.com',
            'comments': nan,
            'serial_num': '1200121107717',
            'model': 'HTS',
            'orient': 'Normal',
            'assays': ',,,'
        }

        self.assertDictEqual(self.plate_1spot.header_data, test_header_1spot)
        self.assertDictEqual(self.plate_4spot.header_data, test_header_4spot)
        self.assertDictEqual(self.plate_7spot.header_data, test_header_7spot)
        self.assertDictEqual(self.plate_10spot.header_data, test_header_10spot)
        self.assertDictEqual(self.plate_384_4spot.header_data, test_header_384_4spot)

    def test_ecl_data(self):

        # check the column names
        test_col_names_96well = [str(x) for x in range(1, 13)]
        test_col_names_96well.insert(0, 'row')
        test_col_names_96well.append('spot')

        test_col_names_384well = [str(x) for x in range(1, 25)]
        test_col_names_384well.insert(0, 'row')
        test_col_names_384well.append('spot')
        
        cols_1spot = list(self.plate_1spot.ecl_data.columns)
        cols_4spot = list(self.plate_4spot.ecl_data.columns)
        cols_7spot = list(self.plate_7spot.ecl_data.columns)
        cols_10spot = list(self.plate_10spot.ecl_data.columns)
        cols_384_4spot = list(self.plate_384_4spot.ecl_data.columns)

        self.assertListEqual(test_col_names_96well, cols_1spot)
        self.assertListEqual(test_col_names_96well, cols_4spot)
        self.assertListEqual(test_col_names_96well, cols_7spot)
        self.assertListEqual(test_col_names_96well, cols_10spot)
        self.assertListEqual(test_col_names_384well, cols_384_4spot)

        # check the dimensions of the data frame
        plate_cols_96well = 12
        plate_cols_384well = plate_cols_96well * 2

        test_ncols_96well = plate_cols_96well + 2 
        test_ncols_384well = plate_cols_384well + 2 

        plate_rows_96well = 8
        plate_rows_384well = plate_rows_96well * 2
        
        test_nrows_96well_1spot = plate_rows_96well
        test_nrows_96well_4spot = plate_rows_96well * 4
        test_nrows_96well_7spot = plate_rows_96well * 7
        test_nrows_96well_10spot = plate_rows_96well * 10

        test_nrows_384well_4spot = plate_rows_384well * 4

        test_dims_96well_1spot = (test_nrows_96well_1spot, test_ncols_96well)
        test_dims_96well_4spot = (test_nrows_96well_4spot, test_ncols_96well)
        test_dims_96well_7spot = (test_nrows_96well_7spot, test_ncols_96well)
        test_dims_96well_10spot = (test_nrows_96well_10spot, test_ncols_96well)

        test_dims_384well_4spot = (test_nrows_384well_4spot, test_ncols_384well)

        self.assertTupleEqual(test_dims_96well_1spot, self.plate_1spot.ecl_data.shape)
        self.assertTupleEqual(test_dims_96well_4spot, self.plate_4spot.ecl_data.shape)
        self.assertTupleEqual(test_dims_96well_7spot, self.plate_7spot.ecl_data.shape)
        self.assertTupleEqual(test_dims_96well_10spot, self.plate_10spot.ecl_data.shape)

        self.assertTupleEqual(test_dims_384well_4spot, self.plate_384_4spot.ecl_data.shape)

        

