#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import img as iimg
from PIL import Image

UNIT_X = 4
UNIT_Y = 6

class VectorSearcher():
  def __init__(self, folder):
    self.data = {}
    for i in xrange(10):
      self.data[i] = []
    for fold in os.listdir(folder):
      for img in os.listdir(folder+'/'+fold):
        if not os.path.isfile(folder+'/'+fold+'/'+img):
          continue
        im = Image.open(folder+'/'+fold+'/'+img)
        a = iimg.Identify()
        size = im.size
        mtx = a.displayize(im, size[0], size[1], False)
        vector = [mtx[i][j] for i in xrange(UNIT_Y) for j in xrange(UNIT_X)]
        self.data[int(fold)].append(vector)

  def dot_product(self, a, b):
    return sum([j*b[i] for i, j in enumerate(a)])
  def magnitude(self, a):
    return sum(j*j for j in a)**(1/2)
  def odchylka(self, a,b):
    return self.dot_product(a,b) / (self.magnitude(a)*(self.magnitude(b)))

  def decide_on(self,vector):
    res = []
    for no, vectors in self.data.iteritems():
      for vec in vectors:
        res.append((self.odchylka(vector, vec),no))
    return sorted(res)
    prumscore = {}
    for i in xrange(10):
      count = sum([1 for b in res if b[1]==i])
      prumscore = sum([b[0] for b in res if b[1]==i])/count
