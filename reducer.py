#!/usr/bin/python
import sys
cur_word = None
cur_count = 0

for line in sys.stdin:
  line = line.strip()
  word,count = line.split("\t",1)

  try:
    count = int(count)
  except:
    count = count #do nothing

  if(cur_word==word):
    cur_count = cur_count+count

  if(cur_word!=word):
    if(cur_word):
      print(cur_word+"\t"+str(cur_count))
    cur_word = word
    cur_count = count
print(cur_word+"\t"+str(cur_count))
