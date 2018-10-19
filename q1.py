# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below

  if(len(portfolios) == 1):
    return portfolios[0]

  answer = 0
  for i in range(16)[::-1]:
    answer <<= 1
    start = {port >> i for port in portfolios}
    answer += any(answer^1 ^ s in start for s in start)
  return answer

# input: [15, 8, 6, 7] output: 15
test1 = [15, 8, 6, 7]
print("Test 1: ",question01(test1))

# input: [9, 7, 12, 2] output: 14
test2 = [9, 7, 12, 2]
print("Test 2: ",question01(test2))

test3 = [6,1,2,3,4,5,6,7,7,8,9,10,11,12,12,13,14,19,1,6,7]
print("Test 3: ",question01(test3))