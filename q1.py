# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  for i in range(16)[::-1]:
    answer <<= 1
    start = {port >> i for port in portfolios}
    answer += any(answer^1 ^ s in start for s in start)
  return answer