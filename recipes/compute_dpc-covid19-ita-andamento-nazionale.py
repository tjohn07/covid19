# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
data_github = dataiku.Folder("iQdwcZ0q")
data_github_info = data_github.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

dpc_covid19_ita_andamento_nazionale_df = ... # Compute a Pandas dataframe to write into dpc-covid19-ita-andamento-nazionale


# Write recipe outputs
dpc_covid19_ita_andamento_nazionale = dataiku.Dataset("dpc-covid19-ita-andamento-nazionale")
dpc_covid19_ita_andamento_nazionale.write_with_schema(dpc_covid19_ita_andamento_nazionale_df)
