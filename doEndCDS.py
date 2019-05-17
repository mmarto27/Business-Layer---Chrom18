#!/usr/bin/env python3
import re
import getLocationCDS

def getEndCDS(input_value, input_value):
     x = getLocationCDS(input_value, input_value)
     coordinate_end = re.findall(r'\-(\d+)', x)

     return coordinate_end
