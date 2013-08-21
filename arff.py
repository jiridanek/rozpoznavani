#features
from __future__ import division

import os
import PIL.Image

import frame
from imageprocessing_helpers import *

class woverh:
  def header(self, out):
    print >>out, "@ATTRIBUTE woverh         numeric"
  def data(self, frame):
    return frame.im.size[0]/frame.im.size[1]

class pctage_covered:
  def header(self, out):
    print >>out, "@ATTRIBUTE pctage_covered numeric"
  def data(self, frame):
    pixels = frame.im.load() # this is not a list, nor is it list()'able
    width, height = frame.im.size

    all_pixels = []
    for x in range(width):
      for y in range(height):
	cpixel = pixels[x, y]
	all_pixels.append(cpixel)
    acc = 0
    for p in all_pixels:
      if p == P_PRESENT:
	acc += 1
    return (acc / (frame.im.size[0] * frame.im.size[1])) * 100

MAXY = 40
MAXX = 20

#normalized to 20*40
class raw_pixels:
  def header(self, out):
    for x in xrange(MAXX):
      for y in xrange(MAXY):
	print >>out, "@ATTRIBUTE p_" + str(x) + "_" + str(y) + " {0,1}"
  def data(self, frame):
    im = frame.im.resize((MAXX, MAXY), PIL.Image.NEAREST)
    pixels = im.load() # this is not a list, nor is it list()'able
    width, height = im.size

    all_pixels = []
    for x in range(width):
      for y in range(height):
	cpixel = "0"
	if pixels[x, y] == P_PRESENT:
	  cpixel = "1"
	all_pixels.append(cpixel)
    return ",".join(all_pixels)

#normalized to 20*40
class borderdist:
  def header(self, out):
    for y in xrange(MAXY):
      print >>out, "@ATTRIBUTE l_" + str(y) + " numeric"
    for y in xrange(MAXY):
      print >>out, "@ATTRIBUTE r_" + str(y) + " numeric"
    for x in xrange(MAXX):
      print >>out, "@ATTRIBUTE t_" + str(x) + " numeric"
    for x in xrange(MAXX):
      print >>out, "@ATTRIBUTE b_" + str(x) + " numeric"
  def data(self, frame):
    im = frame.im.resize((MAXX, MAXY), PIL.Image.NEAREST)
    left = [min(row(im, y)+[MAXY]) for y in xrange(MAXY)] # +[default]
    right = [max(row(im, y)+[0]) for y in xrange(MAXY)]
    top = [min(column(im, x)+[MAXX]) for x in xrange(MAXX)]
    botom = [max(column(im, x)+[0]) for x in xrange(MAXX)]
    return ",".join([",".join(str(x) for x in left), ",".join(str(x) for x in right),",".join(str(x) for x in top),",".join(str(x) for x in botom)])

def column(im, x):
  pixels = im.load()
  p = []
  for y in xrange(im.size[1]):
    if pixels[x, y] == P_PRESENT:
      p.append(y)
  return p
def row(im, y):
  pixels = im.load()
  p = []
  for x in xrange(im.size[0]):
    if pixels[x, y] == P_PRESENT:
      p.append(x)
  return p

def relation(out, name):
  print >>out, "@RELATION " + name
  print >>out
  
def pcls(out):
  print >>out, "@ATTRIBUTE class         {0,1,2,3,4,5,6,7,8,9}"

def data(out):
  print >>out, "@DATA"

def produce_learinig_arff(datadir, arff, features):
  with open(arff, 'w') as out:
    # @relation
    relation(out, "images")
    # @attribute headers
    for f in features:
      f.header(out)
    pcls(out) # class attribute
    # @data header
    data(out)  
    for i in xrange(10): # all classes 0..9
      cls = str(i)
      dt = sorted(os.listdir(os.path.join(datadir, cls)))
      for d in dt:
	strings = [str(f.data(frame.Frame(os.path.join(datadir, cls, d)))) for f in features]
	print >>out, ",".join(strings+[cls]) # attributes + class
	
def produce_arff(datadir, arff, features):
  with open(arff, 'w') as out:
    # @relation
    relation(out, "images")
    # @attribute headers
    for f in features:
      f.header(out)
    #pcls(out) # class attribute
    # @data header
    data(out)  
    dt = sorted(os.listdir(datadir))
    for d in dt:
      strings = [str(f.data(frame.Frame(os.path.join(datadir, d)))) for f in features]
      print >>out, ",".join(strings) # attributes
     
#im = PIL.Image.open('kratsi_ucici_data/8/kratsi_r10_000063.png|3.png')
#produce_learinig_arff('kratsi_ucici_data', 'test.arff', [woverh(),pctage_covered(),borderdist(),raw_pixels()])

produce_arff('kratsi_klasifikace', 'naostro.arff', [woverh(),pctage_covered(),borderdist(),raw_pixels()])