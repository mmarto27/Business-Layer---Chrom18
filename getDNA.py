#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

def getDNA(input_type, input_value):
     dna_sequence = db_query(dbArg7, input_type, input_value)
     
     return dna_sequence
