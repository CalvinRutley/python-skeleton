# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  max = 0
  answer = 0 
  for i in range(0, len(portfolios)-1):
    for j in range(0, len(portfolios)-1):
      Xor = portfolios[i] ^ portfolios[j]
      if (Xor > max):
        max = Xor
        answer = max
  return answer

port = [15,7,23,43,45,5,5,4,64,56,6,7,8,3,5,7]
print(question01(port))