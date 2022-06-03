# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
data_github = dataiku.Folder("iQdwcZ0q")
data_github_info = data_github.get_info()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
df = pd.read_csv(url, index_col=None)
# print(df.head(5))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dpc_covid19_ita_andamento_nazionale_df = pd.DataFrame(df).reset_index()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
dpc_covid19_ita_andamento_nazionale = dataiku.Dataset("dpc-covid19-ita-andamento-nazionale")
dpc_covid19_ita_andamento_nazionale.write_with_schema(dpc_covid19_ita_andamento_nazionale_df)