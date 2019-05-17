#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

def getLocationCDS(input_type, input_value):
     cds_location = db_query(dbArg6, input_value, output_value)
     
     return cds_location

