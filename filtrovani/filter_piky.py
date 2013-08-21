#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def filtr_piky(arr, tresh=6):
  """Requires a sorted list (by time)"""
  time_tresh = 0.3
  filtered = [arr[0]]
  for c,i in enumerate(arr[1:]):
#    print i
#    print filtered
    if abs(int(i[1]) - int(arr[c-1][1])) <= tresh:
      filtered.append(i)
    elif abs(float(i[0]) - float(filtered[-1][0])) >= time_tresh and \
      abs(int(i[1]) - int(filtered[-1][1])) <= tresh + 4:
      filtered.append(i)
  return filtered
	

f = open(sys.argv[1]) # csv file: time,value
records = []
for line in f.readlines():
	segments = [ s.strip() for s in line.split(',') ]
	records.append(segments)
flat = filtr_piky(records)
for line in flat:
	print ",".join(line)
