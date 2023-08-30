import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment(cost):
    maxC = np.max(cost)
    maxCM = maxC - cost
    row, col = linear_sum_assignment(maxCM)
    total = np.sum(cost[row, col])

    
    return row, col, total


n = int(input())
cost = np.array([[int(i) for i in input().split()] for _ in range(n)])
"""
4 2 8
3 5 6
7 1 9
"""
row, col, total = solve_assignment(cost)

print("Assignment:")
for i in range(len(row)):
    print("Task", row[i], "-> Worker", col[i])

print("Total Cost:", total)