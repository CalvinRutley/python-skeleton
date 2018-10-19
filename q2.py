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


cashflow_in = [66, 293, 215, 188, 147, 326, 449, 162, 46, 350]
cashflow_out = [170, 153, 305, 290, 187]
print(question02(cashflow_in,cashflow_out))

# input: (cashflow_in, cashflow_out)
# output: 0

cashflow_in_1 = [189, 28]
cashflow_out_1 = [43, 267, 112, 166]

# input: (cashflow_in, cashflow_out)
# output: 8

print(question02(cashflow_in_1,cashflow_out_1))

cashflow_in_2 = [72, 24, 73, 4, 28, 56, 1, 43]
cashflow_out_2 = [27]

# input: (cashflow_in, cashflow_out)
# output: 1

print(question02(cashflow_in_2,cashflow_out_2))