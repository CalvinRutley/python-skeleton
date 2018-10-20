# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  _ans = 0
  m = 0
  for i in range(31, -1, -1):
    m = m | 1 << i
    _set = set()
    tmp = _ans | 1 << i
    for p in portfolios:
      prefix = p & m
      if prefix ^ tmp in _set:
        _ans = tmp
        break
      _set.add(prefix)
  return _ans