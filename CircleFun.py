import matplotlib
import math
import cmath

# Warum ist die Zahl e so wichtig?
# Die Eulersche Zahl ergibt sich aus a_n=(1+1/n)^n

# def calc_e(N: [int]):
#     return math.pow(1+(1/(math.sqrt(N))),N)

# N_ARR = [1,10,100,10000,9999]
# for N_i in N_ARR:
#     print(calc_e(N_i))
# 85 379 	 80 003 	 87 440 	 83 832 	 75 760 	 72 120 	 73 736 	 78 595 	 73 935 	 79 315 	 85 090

# def calc_cutting_area(d: [float],r1: [float],r2: [float]):
#     cutting_area = 0
#     li = []
#     li.append(r1)
#     li.append(r2)
#     li.sort()
#     if r1+r2 <= d:
#         return cutting_area
#     if d<r1-r2:
#         return cutting_area
R1 = 4 # cm
V1 = (4/3) * math.pi * math.pow(R1,3)
O1 = (4) * math.pi * math.pow(R1,2)
print([V1,O1])