#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import math
import colorsys

from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw

from imageprocessing_helpers import *

class Group:
  def __init__(self, x = 0, y = 0, wx=0, hx=0):
    self.x = x
    self.y = y
    self.wx = wx
    self.hy = hx
  def add_point (self,x, y):
    self.simple_merge(Group(x,y,x,y))
  def interv(self, a1, a2, b1, b2):
    if abs(a1-b1) <=1 or abs(a2-b2) <= 1:
      return True
    if abs(a1-b2) <=1 or abs(a2-b1) <= 1:
      return True
    if a1 > b1 and b2 > a1:
      return True
    if a2 > b1 and b2 > a2:
      return True
    if b2 > a1 and a2 > b2:
      return True
    if b1 > a1 and a2 > b1:
      return True
    return False
  def simple_merge(self, second):
    self.x = min(self.x, second.x)
    self.y = min(self.y, second.y)
    self.wx = max(self.wx, second.wx)
    self.hy = max(self.hy, second.hy)
  def merge(self, dic, lis):
  #  print dic
  #  print lis
    minx = min([dic[i].x for i in lis])
    miny = min([dic[i].y for i in lis])
    maxwx = max([dic[i].wx for i in lis])
    maxhy = max([dic[i].hy for i in lis])
    
    newdic = {}
    i = 0
    for key, val in dic.iteritems():
      if lis.count(key) == 0:
        newdic[i] = val
        i = i+1
    ngr = Group(minx, miny)
    ngr.wx = maxwx
    ngr.hy = maxhy
    newdic[i] = ngr
    return newdic
  def neigh(self, group2):
    if self.interv(self.x, self.wx, group2.x, group2.wx) \
      and self.interv(self.y, self.hy, group2.y, group2.hy):
        return True
    return False

class Frame:
  def __init__(self, fname):
    self.im = self.im = Image.open(fname)
    self.size = self.im.size
    self.pix = self.im.load()
  def crop_multiple(self, boxes):
    """ vrací seznam výřezů """
    images = [self.im.crop((g.x, g.y, g.wx, g.hy)) for g in boxes]
    return images
  def do_treshold(self):
    """ modifikuje pixely obrázku """
    for x in xrange(self.size[0]):
      for y in xrange(self.size[1]):
        r = self.pix[x,y][0] / 255
        g = self.pix[x,y][1] / 255
        b = self.pix[x,y][2] / 255
        hsv = colorsys.rgb_to_hsv(r,g,b)
        h = hsv[0]*360
        s = hsv[1]*100
        v = hsv[2]*100
        #print v
        if h > 150 and h < 185:
          if s >= 50:
            if v >= 65:
              self.pix[x,y] = P_PRESENT
              continue
        self.pix[x,y] = P_ABSENT
  def do_morphology(self):
    """ modifikuje pixely obrázku """
    # moje stare
    self.im = self.im.filter(ImageFilter.MaxFilter())
    self.im = self.im.filter(ImageFilter.MinFilter())
    self.im = self.im.filter(ImageFilter.ModeFilter(5))
    # parametrické otevření vodorovné

    # parametrické otevření svislé

    # zkombinuje

  def segment(self):
    """ vrací seznam souřadnic výřezů """
    pix = self.pix
    im = self.im
    img_size = self.size
    w = img_size[0]
    h = img_size[1]
    cnt_nf = 0
    in_znak = False
    znaky = []
    z_x = 0
    y_min = h+1
    y_max = -1
    for x in xrange(w):
      found = False
      for y in xrange(h):
        if pix[x,y] == P_PRESENT:
          found = True
          y_min = min(y_min, y)
          y_max = max(y_max, y)
          cnt_nf = 0
      if found:
         if in_znak == False:
           in_znak = True
           z_x = x
      else:
        cnt_nf = cnt_nf + 1
        if in_znak == True and cnt_nf > 3:
          znaky.append(Group(z_x, y_min, x-cnt_nf, y_max))
          in_znak = False
          cnt_nf = 0
          y_min = h+1
          y_max = -1
    if in_znak:
      znaky.append(Group(z_x, y_min, w-cnt_nf, y_max))
    #FAIL global rozmery_grup
    #raise Exception
    # skip small areas
    return [g for g in znaky if (g.wx-g.x) > 4 and (g.hy-g.y) > 6]
  def vizualize_boxes(self, boxes):
    im = self.im.copy()
    draw = ImageDraw.Draw(im)
    for box in boxes:
      draw.rectangle((box.wx, box.hy, box.x, box.y), fill=None, outline=(0,255,0))
    im.show()