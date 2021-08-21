#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)<2:
  print("Usage: subtitle_merge.py <file1> <file2>")
  exit(1)

file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'r')

while True:
  # read a block from file1
  block1 = []
  while True:
    line1 = file1.readline()
    if (line1 == "\n"):
      break
    else:
      block1.append(line1.strip('\n\r'))
      
  # read a block from file2
  block2 = []
  while True:
    line2 = file2.readline()
    if (line2 == "\n"):
      break
    else:
      block2.append(line2.strip('\n\r'))

  try:
    # check for mismatches
    if block1[0] != block2[0]:
      print(f"Error in block {block1[0]}")
    else:
      print(block1[0])
      print(block1[1])
      for i in range(2, len(block1)):
        print(block1[i])
      for i in range(2, len(block2)):
        print(block2[i]) 
  
    print("")
  except:
    exit(0)
       
file1.close()
file2.close()