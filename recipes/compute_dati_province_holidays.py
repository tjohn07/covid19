# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import holidays

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
it_holidays = holidays.Italy(years=[2019, 2020, 2021, 2022])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
dati_province_prepared = dataiku.Dataset("dati_province_prepared")
dati_province_prepared_df = dati_province_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dati_province_prepared_df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for date in it_holidays.items():
    print(date)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dati_province_prepared_df['data'] in it_holidays

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for row in dati_province_prepared_df['data']:
    if row in it_holidays:
        print(row)
        dati_province_prepared_df['holiday'] = 1
#     else:
#         dati_province_prepared_df['holiday'] = 0

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dati_province_prepared_df['holiday'].value_counts()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dati_province_prepared_df.info()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

dati_province_holidays_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
dati_province_holidays = dataiku.Dataset("dati_province_holidays")
dati_province_holidays.write_with_schema(dati_province_holidays_df)