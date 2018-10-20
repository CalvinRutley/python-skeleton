# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  ans, m = 0, 0
  for i in range(31,-1,-1):
    temp = ans | 1 << i
    m = m | 1 << i
    bits = set()
    for p in portfolios:
      bits.add(p & m)
    for bit in bits:
      if bit ^ temp in bits:
        ans = temp
        break
  return ans