#!/usr/bin/env python3
import re
import getLocationCDS

def getStartCDS(input_value, input_value):
     x = getLocationCDS(input_value, input_value)
     coordinate_start = re.findall(r'(\d+)\-', x)

     return coordinate_start
