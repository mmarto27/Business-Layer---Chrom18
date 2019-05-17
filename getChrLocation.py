#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

def getChrLocation(input_type, input_value):
     chr_location = db_query(dbArg2, input_type, input_value)
     if chr_location == '':
          return 'Chromosomal Location Missing'
     else:
          return chr_location
