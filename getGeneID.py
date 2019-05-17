#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

def getGeneID(input_type, input_value):
     gene_id = db_query(dbArg3, input_type, input_value)
     if gene_id == '':
          return 'Gene ID missing'
     else:
          return gene_id
