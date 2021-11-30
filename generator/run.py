#!/usr/bin/env python3
from generator import gen_url
import sys

try: 
    cant = int(sys.argv[1])
except:
    cant = 5
try:
    valormagico = int(sys.argv[2])
except:
    valormagico = 20
gen_url(cant, True, valormagico)
