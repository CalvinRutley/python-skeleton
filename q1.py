# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  for i in range(0, len(portfolios)-1):
    answer = portfolios[i] ^ portfolios[i+1]
  return answer

port = [15,7]
print(question01(port))