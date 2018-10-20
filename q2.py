# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below
  psCashIn = recursive_power_set(cashFlowIn)
  psCashOut = recursive_power_set(cashFlowOut)

  min = 9223372036854775807

  for i in range(1, len(psCashIn)):
    for j in range(1, len(psCashOut)):
      tot = abs(sum(psCashIn[i]) - sum(psCashOut[j]))
      if (tot < min):
        min = tot
      if (min == 0):
        return 0

  return min


def recursive_power_set(items):
    if not items:
        return [[]]
    e = items.pop()
    ps = recursive_power_set(items)
    ps.extend([i + [e] for i in ps])
    return ps