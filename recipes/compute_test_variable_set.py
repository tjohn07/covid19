# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



from dataiku.scenario import Trigger
import dataiku

# Accessing the DSS Global/Project Variables
proj = dataiku.Project()
variables = proj.get_variables()

# Create a list of current files in the managed folder.
file_list = test_folder.list_paths_in_partition()

# Create a list of currently existing global/project variables to test if our length_list has been set.
global_check = list(variables['standard'].keys())

# Testing to see if the length_list global/project variable exists.
# If it does not, it will be created.
if 'length_list' not in global_check:
    length_list = len(file_list)
    variables['standard'] = {"length_list" : length_list}
    proj.set_variables(variables)

# If it does exist, the code continues running to the next step.
else:
    continue

# Create variables that we'll use to test the file list length.
current_length_list = len(file_list)
var_length_list = int(dataiku.get_custom_variables().get("length_list"))
t = Trigger()

# For loop to check if the trigger file name already exists in the Managed folder.
# Once the trigger file is added (in this example "trigger_file.txt"),
# the count variables keep the scenario from running indefinitely.
for file in file_list:
    if current_length_list > var_length_list and file == '/trigger_file.txt':
        t.fire()

# Now we reset the results as DSS Global/Project variables.
variables['standard'] = {"length_list" : current_length_list}
proj.set_variables(variables)