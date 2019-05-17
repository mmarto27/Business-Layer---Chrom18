#!/usr/bin/env python3
import doSelectCDS
import doEcoRI
import doBamHI
import doBsuMI
import re

def doRestrictionEnzymes(input_type, input_value):
     x = doSelectCDS(input_type, input_value)
     y = doEcoRI(x)
     z = doBamHI(y)
     dna_sequence = doBsuMI(z)
     
     return dna_sequence
