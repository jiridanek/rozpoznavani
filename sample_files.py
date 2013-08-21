import os
import random
import shutil

def sample_files(fr, to, n):
  files = sorted(os.listdir(fr))
  sample = random.sample(files, n)
  for f in sample:
    shutil.copy(os.path.join(fr, f), to)