#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw

import operator
import os
import re
import math

from img_processing import *
from vector_searcher import *
from helpers import *


#http://stackoverflow.com/questions/3917601/ffmpeg-split-avi-into-frames-with-known-frame-rate
#http://linuxers.org/tutorial/how-extract-images-video-using-ffmpeg
#http://ubuntuforums.org/showthread.php?t=1484695

DATA_DIR = "sablony"
global UNIT_X
global UNIT_Y
UNIT_X = 4
UNIT_Y = 6
#UNIT_X = 3
#UNIT_Y = 5

class Identify():
  """
  Umí buď vektor search mezi ručně vytvořenými vzory,
  nebo porovnávat s ručně vytvořenými maskami.
  
  Přepíná se mezi tím 
  """
  def __init__(self, images=None):
    self.images = images
    self.masks = None
  def load_masks(self):
    self.masks = {}
    for i in xrange(10):
      no = Image.open(DATA_DIR + "/%(n)s.png" % {'n': i})
      mask = self.displayize(no, UNIT_X,UNIT_Y)
      self.masks[i] = mask

  def identify(self, table):
    results = {}
	
    for no, mask in self.masks.iteritems():
  #		print "proveruju ", no
      score = 0
      for x in xrange(UNIT_Y):
        for y in xrange(UNIT_X):
          if mask[x][y] > 2 and table[x][y] > 1:
  #					print "shoda"
            score = score + 1
#            score = score + table[x][y]
          elif mask[x][y] < 3 and table[x][y] < 2:
  #					print "shoda"
             score = score + 1
#            score = score + (8-table[x][y])
          else:
  #					print "neshoda"
            score = score - 1
#            score = score - table[x][y]
      results[no] = score
    return results
	
  def displayize(self,pic, w, h, tresholding=True):
    disp = {}
    mtx = initize_array(UNIT_Y, UNIT_X)
#    print w
#    print h
#    print '===='
    for i in xrange(UNIT_Y):
      for j in xrange(UNIT_X):
##        print '===='
#        print w
#        print h
        #pic.show()
        x_dil = w//UNIT_X
        y_dil = h//UNIT_Y
        el = (j*x_dil, i*y_dil, \
          w-(UNIT_X-j-1)*x_dil, h-(UNIT_Y-i-1)*y_dil)
#        print el
        cnt = self.count_b_pix(pic, el)/(w*h/(UNIT_X*(UNIT_Y)))
#        print cnt
        if tresholding:
          s = 0
          if cnt > 10/49:
            s = 1
          if cnt > 20/49:
            s = 2
          if cnt > 25/49:
            s = 3
          if cnt > 30/49:
            s = 4
          if cnt > 35/49:
            s = 6
          if cnt > 42/49:
	      	 	s = 8
          mtx[i][j] = s 
        else:
          mtx[i][j] = cnt
    return mtx
  def could_be_1(self, im):
    """pokud je číslovka hodně protáhlá, je to natvrdo jednička
    kdyby to tu nebylo, často je jednička rozpoznána jako osmička
    """
    size = im.size
    return (size[0] / size[1]) < 6/16
  def count_b_pix(self,img, box):
    return img.crop(box).histogram()[0]
	#FIXME
  def result(self, useVectors = False):
    if useVectors:
      a = VectorSearcher("vec")
    res = []
    detaily = []
    for im in self.images:
      
      si = im.size
      tabl = self.displayize(im, si[0], si[1])
      if self.could_be_1(im):
        res.append(1)
        continue
      if useVectors:
        tabl = self.displayize(im, si[0], si[1], False)
        vector = [tabl[i][j] for i in xrange(UNIT_Y) for j in xrange(UNIT_X)]
        r = sorted(a.decide_on(vector))
        r.reverse()
        ##print r
        #print
        #
        res.append(r[0][1])
        detaily.append([r])
      else:
        r = (sorted(self.identify(tabl).iteritems(), key=operator.itemgetter(1)))
        r.reverse()
        res.append(r[0][0])
        res = res
    return [res, detaily]

 





oks = 0
noks = 0
fails = []

indie = 0
"""
for f in os.listdir("."):
  m = re.match("([0-9]*)(_)*.png",f)
  if m:
    IMAGE = m.group(0)

    i = ImgProcessing()
    i.load_image(IMAGE)
    i.drop_uninteresting_colors()
    numbers = i.extract_numerals()[0]

    a = Identify(numbers)
    a.load_masks()
    print m.group(1)
    cis = cislo_do_pole(int(m.group(1)))
    for i, j in enumerate( a.result()):
      if j == cis[i]:
        print "ok"
        oks = oks+1
#        numbers[i].save(str(cis[i]) + "/_" + str(indie) + ".png")
#        indie = indie+1
      else:
        print "nok"
        noks = noks+1
        fails.append((cis[i], j))
#        numbers[i].save(str(cis[i]) + "/|" + str(indie) + ".png")
#        indie = indie+1
"""  

#im.show()
#im_2.show()

def file_to_numerals(img_file):
  i = ImgProcessing()
  i.load_image(img_file)
  i.drop_uninteresting_colors()
#  global nums
  nums = i.find_numerals()
  rot = i.get_rotation_fix(nums)
#  global pics
  pics = i.extract_numerals(nums)
#  global res
  res = []
  for pic in pics:
    obr = pic.copy().rotate(rot, expand=True)
    res.append(i.extract_numerals(i.find_numerals(obr), obr)[0])
  return res

if __name__ == "__main__":
  global i

  

   
  
  
