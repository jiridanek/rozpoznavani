import os

import frame

def prepare_learning_set(fr, to):
  for f in os.listdir(fr):
    #import pdb; pdb.set_trace()
    img = frame.Frame(os.path.join(fr,f))
    img.do_treshold()
    img.do_morphology()
    boxes = img.segment()
    segments = img.crop_multiple(boxes)
    for i,s in enumerate(segments):
      s.save(os.path.join(to, f + "|" + str(i) + ".png"))