# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

class TrieNode():
  zero = None
  one = None
  value = None

# modify this function, and create other functions below as you wish
def question01(portfolios):
  root = TrieNode()
  bits = range(31,-1,-1)

  for p in portfolios:
    current = root
    for i in bits:
      m = 1 << i
      mp = p & m

      if mp is 0:
        if not current.zero:
          current.zero = TrieNode()
        current = current.zero
      else:
        if not current.zero:
          current.one = TrieNode()
        current = current.one
    current.value = p
  
  answer = 0
  for p in portfolios:
    current = root
    for i in bits:
      m = 1 << i
      mp = p & m

      if mp is 0:
        if current.one:
          current = current.one
        else:
          current = current.zero
      else:
        if current.zero:
          current = current.zero
        else:
          current = current.one
    temp_max = p ^ current.value
    if temp_max > answer:
      answer = temp_max
  
  return answer