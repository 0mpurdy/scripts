# Convert raw pnm file into black and white pixel grid where
# 1 = black
# 0 = white

import os

def writeFile(text2d, fileNumber):
  outFile = open("two_" + str(fileNumber) + ".csv", "w")  
  for row in text2d:
    writeRow = ','.join(str(e) for e in row)
    outFile.write("%s\n" % writeRow)

def readFile(fileNumber):
  read_file = open("Untitled" + str(fileNumber) + ".pnm", "r")
  return read_file.read()

def create2d(text1d):
  text2d = []
  index = 0
  black_pixel = '0'
  while (index < img_width * img_height):
    row = index % img_width
    col = index // img_height
    if (col == 0): text2d.append([])
    text2d[col].append(1 if text1d[index] == black_pixel else 0)
    index += 1
  return text2d
    
img_width = 16
img_height = 16

for count in range(10):
  file_text = readFile(count)
  text2d = create2d(file_text.split("\n")[3:])
  writeFile(text2d, count)
