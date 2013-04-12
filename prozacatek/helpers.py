#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def initize_array(y, x):
	return [[0]*x for i in range(y)]

def flatten_sorted_array(arr):
  flattened = [arr[0]]
  for i in arr:
    if i != flattened[-1]:
      flattened.append(i)
  return flattened

def cislo_do_pole(cislo):
  out = []
  while cislo > 0:
    out.append(cislo % 10)
    cislo = cislo // 10
  out.reverse()
  return out
  
def rotate(element, angle):
  if angle <= 0:
    return element
  elif angle == 1:
    element.reverse()
    wh = len(element)
    out = initize_array(wh, wh)
    try:
      for l in xrange(wh):
        for c in xrange(wh):
          out[l][c] = element[c][l]
    except Exception,e:
      raise Exception
    return out
  elif angle == 2:
    out = rotate(rotate(element,1), angle-1)  
    return out #rotate(rotate(element,1), angle-1)
  elif angle == 3:
    return rotate(rotate(element,1), angle-1)

def subtract(a, b):
  w_a = len(a)
  h_a = len(a[0])
  w_b = len(b)
  h_b = len(b[0])
  out = initize_array(max(w_a, w_b), max(h_a, h_b))
  
  for x in xrange(max(w_a, w_b)):
    for y in xrange(max(h_a, h_b)):
      a_val = a[x][y] if x < w_a and y < h_a else 0
      b_val = b[x][y] if x < w_b and y < h_b else 0
      if a_val == 1 and b_val == 1:
        out[x][y] = 0
      elif a_val == 1 and b_val == 0:
        out[x][y] = 1
      else:
        out[x][y] = 0
  return out

def disjunkce(a, b):
  w_a = len(a)
  h_a = len(a[0])
  w_b = len(b)
  h_b = len(b[0])
  out = initize_array(max(w_a, w_b), max(h_a, h_b))
  
  for x in xrange(max(w_a, w_b)):
    for y in xrange(max(h_a, h_b)):
      a_val = a[x][y] if x < w_a and y < h_b else 0
      b_val = b[x][y] if x < w_b and y < h_b else 0
      if  a_val == 1 or b_val == 1:
        out[x][y] = 1
      else:
        out[x][y] = 0
  return out


  
  
