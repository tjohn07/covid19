# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv'
df = pd.read_csv(url, index_col=None)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
province_df = pd.DataFrame(df).reset_index()

# Write recipe outputs
dati_province = dataiku.Dataset("dati_province")
dati_province.write_with_schema(province_df)