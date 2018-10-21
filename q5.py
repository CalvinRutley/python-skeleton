# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING
from __future__ import division
import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  def helper(idx, a, nAlloc):
    global ans
    lowerBound = nAlloc + (a + sortedShares[idx] -1) / sortedShares[idx]

    if lowerBound >= ans:
      return
    if a == sortedShares[idx] and nAlloc + 1 < ans:
      ans = nAlloc + 1
      return
    if a > sortedShares[idx]:
      helper(idx, a - sortedShares[idx], nAlloc + 1)
    if idx < len(sortedShares) -1:
      helper(idx + 1, a, nAlloc)
  
  if len(allowedAllocations) == 0:
    return -1
  if totalValue == 0:
    return 0
  
  sortedShares = sorted(allowedAllocations, reverse=True)
  upperBound = (totalValue + sortedShares[-1] -1) / sortedShares[-1] + 1

  global ans
  ans = upperBound

  helper(0, totalValue, 0)

  if ans == upperBound:
    return -1
  else:
    return ans