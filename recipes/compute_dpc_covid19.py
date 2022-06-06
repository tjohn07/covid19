# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
df = pd.read_csv(url, index_col=None)
# print(df.head(5))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dpc_covid19_ita_andamento_nazionale_df = pd.DataFrame(df).reset_index()

# Write recipe outputs
dpc_covid19 = dataiku.Dataset("dpc_covid19")
dpc_covid19.write_with_schema(dpc_covid19_df)
