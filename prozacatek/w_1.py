#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from img import *

import os
import re

for f in os.listdir("ucici_data2"):
  m = re.match("([0-9]*)(_)*.png",f)
  if m:
    IMAGE = 'ucici_data2/' + m.group(0)

    numbers = file_to_numerals(IMAGE)

    a = Identify(numbers)
    print m.group(1)
    cis = cislo_do_pole(int(m.group(1)))
    global result 
    a.load_masks()
    result = a.result(useVectors=False)
    for i, j in enumerate( result[0]):
      print i, ' ', j
      if j == cis[i]:
        print "ok"
        oks = oks+1
        numbers[i].save("vec/" + str(cis[i]) + "/_" + str(indie) + ".png")
        indie = indie+1
      else:
        print "nok"
        noks = noks+1
        print 'fail: ',cis[i], ' ', j
        fails.append((cis[i], j))
        numbers[i].save("vec/" + str(cis[i]) + "/|" + str(indie) + ".png")
        indie = indie+1

"""
IMAGE = 'testovaci_data/1177.png'
i = ImgProcessing()
i.load_image(IMAGE)
i.drop_uninteresting_colors()
numbers = i.extract_numerals()[0]
"""
"""
numbers[2].size
b = Identify()
mtx = b.displayize(numbers[2], 19, 38, False)
vector = [mtx[i][j] for i in xrange(UNIT_Y) for j in xrange(UNIT_X)]


a = VectorSearcher("vec")
print a.decide_on(vector)
"""

"""	a = (0, 0, w, h//5)
	b = (2*(w//3), 0, 3*(h//5), h)
	c = (2*(w//3), 2*(h//5), h)
	c = (0, 4*(h//5), w,h)
	d = ()
"""



"""
150 - 185
50
90
"""
