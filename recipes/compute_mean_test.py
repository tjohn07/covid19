# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
dati_province = dataiku.Dataset("dati_province")
dati_province_df = dati_province.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

mean_test_df = dati_province_df # For this sample code, simply copy input to output


# Write recipe outputs
mean_test = dataiku.Dataset("mean_test")
mean_test.write_with_schema(mean_test_df)
