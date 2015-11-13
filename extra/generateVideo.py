import cv2
from sys import argv
import numpy as np
import scipy.ndimage as nd
import os

def listFrames(path):
  fns = os.listdir(path)
  fns = [path + '/' + x for x in fns]
  fns = filter(lambda x: x.endswith('.jpg'), fns)
  fns.sort()
  return fns

def getWriter(fns, path):
  if path.endswith('/'):
    path = path[:-1]
  fn = path + '.out.avi'
  h, w, d = cv2.imread(fns[0]).shape
  return cv2.VideoWriter(fn, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 24, (w, h))

def addStaticFrame(writer, index, frames):
  image = cv2.imread(fns[index])
  for i in range(frames):
    writer.write(image)


if __name__ == '__main__':
  if len(argv) < 3:
    print 'Usage: python %s <source_image> <generated_folder>' % argv[0]
    print 'ex: python %s source.jpg frames/' % argv[0]
    exit()

  path = argv[2]
  fns = [argv[1]]
  fns.extend(listFrames(path))

  writer = getWriter(fns, path)

  addStaticFrame(writer, 0, 12);

  fadeFrames = 24
  for index in range(len(fns)-1):
    image = cv2.imread(fns[index])
    next_ = cv2.imread(fns[index+1])
    for i in range(0, fadeFrames):
      out_ = image / float(fadeFrames) * (fadeFrames-i) + \
             next_ / float(fadeFrames) * i
      writer.write(out_.astype('uint8'))

  addStaticFrame(writer, -1, 12);

  writer.release()
