# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
# from dataiku.scenario import Trigger


# Accessing the DSS Global/Project Variables
proj = dataiku.Project()
variables = proj.get_variables()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# declare the datasets being used from the flow
ntile10_dataset = dataiku.Dataset("dpc_covid19_prepared_windows_by_ntile10")
dpc_dataset = dataiku.Dataset("dpc_covid19_prepared")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#  declare datasets as dataframes
ntile10_df = ntile10_dataset.get_dataframe()
dpc_df = dpc_dataset.get_dataframe()


# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#Set project variables for ntile ranges from ntile_range_dataset in order to compare to full dataset
for num in range(1,11):
    variables["standard"][f'n{num}'] = range(int(ntile10_df['nuovi_positivi_min'][ntile10_df['ntile10'] == num]), int(ntile10_df['nuovi_positivi_max'][ntile10_df['ntile10'] == num]+1))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
ntile_dict = {}
for row in dpc_df['nuovi_positivi']:
    for ntile in range(1,11):
        if row in variables["standard"][f'n{ntile}']:
            ntile_dict[row] = int(ntile)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dpc_df['ntile'] = dpc_df['nuovi_positivi'].map(ntile_dict)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
test_variable_set = dataiku.Dataset("test_variable_set")
test_variable_set.write_with_schema(dpc_df)