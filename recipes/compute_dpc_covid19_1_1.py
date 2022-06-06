# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
df = pd.read_csv(url, index_col=None)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
regione_df = pd.DataFrame(df).reset_index()

# Write recipe outputs
dati_regione = dataiku.Dataset("dati_regione")
dati_regione.write_with_schema(regione_df)