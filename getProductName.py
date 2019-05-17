#!/usr/bin/env python3
from SQL_python_functions import db_query
from configFile import *

def getProductName(input_type, input_value):
     product_name = db_query(dbArg4, input_type, input_value)
     if product_name == '':
          return 'Product Name Missing'
     else:
          return product_name
