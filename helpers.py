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