#!/usr/bin/env python3
import getStartCDS
import getEndCDS
import getDNA
import re

def doSelectCDS(input_type, input_value):
     start_cds = getStartCDS(input_type, input_value)
     end_CDS = getEndCDS(input_type, input_value)
     dna_sequence = getDNA(input_type, input_value)

     dna_selected_cds = ''

     count_start = -1
     for x in start_cds:
          dna_selected_cds = dna_sequence[:int(x)+count_start] \
                             + cds_start_char + dna_sequence[int(x)+count_start:]
          count_start += 1

     count_end = 1
     for x in end_cds:
          dna_selected_cds = dna_selected_cds[:int(x)+count_end] \
                             + cds_end_char + dna_selected_cds[int(x)+count_end:]
          count_end += 2
     
     return dna_selected_cds
