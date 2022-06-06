# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
dati_province_prepared = dataiku.Dataset("dati_province_prepared")
dati_province_prepared_df = dati_province_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

dati_province_holidays_df = dati_province_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
dati_province_holidays = dataiku.Dataset("dati_province_holidays")
dati_province_holidays.write_with_schema(dati_province_holidays_df)
