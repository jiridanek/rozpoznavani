#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from img import *
from multiprocessing import Pool

import os
import re

def ocr(f):
  m = re.match("delsi_r10_([0-9]*)(_)*.png",f)
  if m:
#    if int(m.group(1)) == 6:
#      raise Exception
    #try:
    IMAGE = FOLDER+'/' + m.group(0)

    numbers = file_to_numerals(IMAGE)

    a = Identify(numbers)
#    print m.group(1)
    global result 
    vectors = True
    if not vectors:
      a.load_masks()
    result = a.result(useVectors=vectors)
    if vectors:
      minimalka = min([prav[0][0] for prav in result[1]])
      return str(int(m.group(1))/10) + ',' + "".join([str(b) for b in result[0]]) + ',' + str(minimalka[0]) + ',' + str(minimalka[1])
    else:
      return str(int(m.group(1))/10) + ',' + "".join([str(b) for b in result[0]])
    #except Exception as e:
    #  return "FAIL" + str(e)

debug=True

FOLDER = "../data/delsi"

files = sorted(os.listdir(FOLDER))

if debug:
  for i in files:
    print ocr(i)

pool = Pool(processes=4)
mapa = pool.map(ocr, files)
for i in mapa:
  print i
