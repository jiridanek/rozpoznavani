#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def filtr_nejiste(arr, tresh=0.85):
  """Requires a sorted list"""
  filtered = []
  for i in arr:
#    print i
#    print filtered
    if float(i[2]) > tresh:
      filtered.append(i)
  return filtered
	

f = open(sys.argv[1])
records = []
for line in f.readlines():
	segments = [ s.strip() for s in line.split(',') ]
	records.append(segments)
flat = filtr_nejiste(records)
for line in flat:
	print ",".join(line)
