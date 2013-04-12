#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import colorsys

from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw

from helpers import *
import math

P_PRESENT=(255,255,255)
P_ABSENT=(0,0,0)

class ImgProcessing():
  def __init__(self):
    self.im = None
  def load_image(self,imgfile):
    self.im = Image.open(imgfile)
#    self.im.show()
    size = self.im.size
    self.pix = self.im.load()

  def save_numerals(self,):
    pass
  
  def extract_numerals(self,boxes,image=None):
    if image:
      pix = image.load()
      im = image
    else:
      pix = self.pix
      im = self.im
    images = [im.crop((g.x, g.y, g.wx, g.hy)) for g in boxes]
    return images
  """
    groups = {}

    size = self.im.size

    for x in xrange(size[0]):
      for y in xrange(size[1]):
        if self.pix[x,y] == P_PRESENT:
          matches = []

          for no, gr in groups.iteritems():
            if Group(x,y,x,y).neigh(gr):
              matches.append(no)
          try:
            groups[max(groups.keys()) + 1] = Group(x,y,x,y)
          except ValueError:
            groups[0] = Group(x,y,x,y)
          if len(matches) != 0:
            matches.append(max(groups.keys()))
            groups = Group().merge(groups, matches)
    rot_fix = self.get_rotation_fix(groups)
    images = [self.im.crop((g.x, g.y, g.wx, g.hy)) for g in  groups.values() if (g.wx-g.x) > 3 and (g.hy-g.y) > 5]
    return (images, rot_fix)
  """
  """
  def extract_numerals(self,):
    img_size = self.im.size
    pole = initize_array(img_size[0], img_size[1])
    smery = [(i,j) for i in [-1,0,1] for j in [-1,0,1] if (i != 0 or j != 0) ]
    w = img_size[0]
    h = img_size[1]
    n_grupa = 1
    rozmery_grup = {}
    for x in xrange(w):
      for y in xrange(h):
        if self.pix[x,y] == P_PRESENT:
          sousedi = [(x+ab[0], y+ab[1]) for ab in smery \
            if x+ab[0] <= w and y+ab[1] <= h and x+ab[0] >=0 and y+ab[1]>=0]
          grupy = sorted([pole[s[0]][s[1]] for s in sousedi])
          if pole[x][y] != 0:
            rozmery_grup[pole[x][y]] = add_point(x,y,x,y)
          elif max(grupy) == 0:
            pole[x][y] = n_grupa
            rozmery_grup[n_grupa] = Group(x,y,x,y)
            n_grupa = n_grupa + 1
          else:
            grupy = flatten_sorted_array(grupy)
            grupy = filter((lambda x: x != 0),grupy)
            if(len(grupy) == 1):
              pole[x][y] = grupy[0]
              rozmery_grup[grupy[0]].add_point(x,y)
            else:
              pole[x][y] = grupy[0]
              prvni = rozmery_grup[grupy[0]]
              prvni.add_point(x,y)
              ostatni = grupy[1:]
              for o in ostatni:
                prvni.simple_merge(rozmery_grup[o])
                rozmery_grup[o] = rozmery_grup[grupy[0]]
#              print "dve grupy"
#          FAIL!!!
#          for s in sousedi:
#            a,b = s
#            if self.pix[a,b] == P_PRESENT:
#              pole[a][b] = pole[x][y]
         
    #FAIL global rozmery_grup
    #raise Exception
    rozmery_grup_a = flatten_sorted_array(sorted(rozmery_grup.values()))
    images = [self.im.crop((g.x, g.y, g.wx, g.hy)) for g in  rozmery_grup_a if (g.wx-g.x) > 3 and (g.hy-g.y) > 5]
    return images
  """
  
  def drop_uninteresting_colors(self):
    size = self.im.size
    for x in xrange(size[0]):
      for y in xrange(size[1]):
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
            else:
              self.pix[x,y] = P_ABSENT
          else:
            self.pix[x,y] = P_ABSENT
        else:
          self.pix[x,y] = P_ABSENT
  def do_filtering(self):
    self.im = self.im.filter(ImageFilter.MaxFilter())
    self.im = self.im.filter(ImageFilter.MinFilter())
    self.im = self.im.filter(ImageFilter.ModeFilter(5))
  def get_rotation_fix(self, boxes):
    fst = self.middle_point(boxes[0])
    cumul = 0
    try:
      boxes = boxes.values()
    except Exception:
      pass
    for box in boxes[1:]:
      if (box.wx-box.x) > 3 and (box.hy-box.y) > 5:
        pos = self.middle_point(box)
        dy = pos[1] - fst[1]
        dx = pos[0] - fst[0] 
        cumul = cumul + (dy/dx)
    return math.degrees(math.atan(cumul/len(boxes)))
    
  def middle_point(self, box):
    return ((box.x + box.wx) / 2, (box.y + box.hy) / 2)

  def find_numerals(self,image = None):
    if image:
      pix = image.load()
      im = image
    else:
      pix = self.pix
      im = self.im
    img_size = im.size
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
    return [g for g in znaky if (g.wx-g.x) > 4 and (g.hy-g.y) > 6]
  def show_boxes(self,boxes):
    im = self.im.copy()
    draw = ImageDraw.Draw(im)
    for box in boxes:
      draw.rectangle((box.wx, box.hy, box.x, box.y), fill=None, outline=(0,255,0))
    im.show()
  def m_open(self):
    pass
  def m_erode(self, element):
    pass
  def m_dilate(self, element):
    pass
  def m_hit_a_miss(self, img, element=[[]]):
    #(wh//2)
    w = len(img)
    h = len(img[0])
    wh = len(element)
    output = initize_array(w,h)
    for x in xrange(w):
      for y in xrange(h):
        match = True
        for xa in xrange(wh):
          for ya in xrange(wh):
            dxa = xa-(wh//2)
            dya = ya-(wh//2)
            try:
              if img[x+dxa][y+dya] == 1:
                pval = 1 
              else:
                pval = 0

              if x+dxa < 0 or y+dya < 0:
                pval = 0
            except Exception, e:
              pval = 0
            if pval != element[xa][ya] and element[xa][ya] != None:
              match = False
        output[x][y] = 1 if match == True else 0
    return output
  
  def m_id(self):
    (w, h) = self.im.size
    output = initize_array(w,h)
    for x in xrange(w):
      for y in xrange(h):
        output[x][y] = 1 if self.pix[x,y] == P_PRESENT else 0
    return output
            
  def m_thin(self, what = None):
    """ http://homepages.inf.ed.ac.uk/rbf/HIPR2/thin.htm """
    
    if what == None:
      what = self.m_id()
    
    el_a = [[0,0,0],
            [None, 1, None],
            [1,1,1]]
    el_b = [[None, 0,0],
            [1,1,0],
            [None, 1, None]]
    al_b = [[0, None, None],
            [0, 1, 0],
            [0,0,0]]
    el_1 = [[None, 0, None],
            [None,1,None],
            [1,1,1]]
    el_2 = [[0, None, None],
            [None,1,None],
            [1,None,0]]
    el_3 = [[None, None, 0],
            [None,1,None],
            [1,None,None]]

    elments = []
    for angle in xrange(4):
      elments.append(rotate(el_a, angle))
#      elments.append(rotate(el_1, angle))
#      elments.append(rotate(el_2, angle))
#      elments.append(rotate(al_b, angle))
      elments.append(rotate(el_b, angle))
#    print elments
    hams = map(lambda x: self.m_hit_a_miss(what, x), elments)
    ham = reduce(disjunkce, hams[1:], hams[0])
    #return ham
    output = subtract(what, ham)
    return output

def fromArray(array):
  w = len(array)
  h = len(array[0])
  
  im = Image.new("RGB", (w, h))
  pix = im.load()
  
  for x in xrange(w):
    for y in xrange(h):
      pix[x,y] = P_PRESENT if array[x][y] == 1 else P_ABSENT
  return im


i = ImgProcessing()
"""
i.load_image('testovaci_data/1219.png')
i.drop_uninteresting_colors()
"""

def m_id(im):
  (w, h) = im.size
  pix = im.load()
  output = initize_array(w,h)
  for x in xrange(w):
    for y in xrange(h):
      output[x][y] = 1 if pix[x,y] == P_PRESENT else 0
  return output

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

if __name__ == 'main':
  numbers = file_to_numerals('testovaci_data/1219.png')
  i = ImgProcessing()

  a = m_id(numbers[1])

  dlouhy=[[None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None],
          [None, None, None,None,1,None,None,None, None]]
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)
  a = i.m_thin(a)


  #kratsi=[[None, 1, None], [None, 1, None], [None,1, None]]
  #a = i.m_hit_a_miss(a, rotate(kratsi,0))


  fromArray(a).show()

