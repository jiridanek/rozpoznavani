#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def flatten_sorted_array(arr, key=(lambda x:x)):
  flattened = [arr[0]]
  for i in arr:
    if key(i) != key(flattened[-1]):
      flattened.append(i)
  return flattened
	

f = open(sys.argv[1])
records = []
for line in f.readlines():
	segments = [ s.strip() for s in line.split(',') ]
	records.append(segments)
flat = flatten_sorted_array(records, key=(lambda x:x[1]))
for line in flat:
	print ",".join(line)
