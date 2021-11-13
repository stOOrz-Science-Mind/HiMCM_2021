import math

KEV = 273.15
MONTHS_IN_YEAR = 12

SIDE_SLOPE = 0.8902 * 2
LAKE_DEPTH = 162
SURFACE_ELEVATION = 375
BOTTOM_TO_SEA = SURFACE_ELEVATION - LAKE_DEPTH

LENGTH_TOP = math.sqrt(640) * 1000
LENGTH_BOTTOM = LENGTH_TOP - (2 * LAKE_DEPTH) / SIDE_SLOPE

x = LAKE_DEPTH * LENGTH_BOTTOM / (LENGTH_TOP - LENGTH_BOTTOM)
# print(x)
# water and vapor equilibrium
# f(x) = a*exp(-b/x)

PRE_CONST = 1.447e+11
EXP_CONST = 5259

MONTH_TEMPERATURE_MIN = [1, 3, 5, 7, 12, 1, 22, 21, 15, 8, 3, 1]
for i in range(len(MONTH_TEMPERATURE_MIN)) :
    MONTH_TEMPERATURE_MIN[i] = MONTH_TEMPERATURE_MIN[i] + KEV

MONTH_TEMPERATURE_MAX = [16, 18, 23, 28, 33, 38, 41, 40, 36, 29, 21, 15]
for i in range(len(MONTH_TEMPERATURE_MAX)) :
    MONTH_TEMPERATURE_MAX[i] = MONTH_TEMPERATURE_MAX[i] + KEV

# print(len(MONTH_TEMPERATURE_MIN))
# print(len(MONTH_TEMPERATURE_MAX))
# print(MONTH_TEMPERATURE_MIN)
# print(MONTH_TEMPERATURE_MAX)

TEMPERATURE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(MONTHS_IN_YEAR) :
    TEMPERATURE[i] = (MONTH_TEMPERATURE_MIN[i] + MONTH_TEMPERATURE_MAX[i]) / 2


def length(depth) :
    return (LENGTH_BOTTOM + 2 * depth / SIDE_SLOPE)


def area(depth) :
    # depth refers to the distance between a certain depth and the bottom of the lake.
    return length(depth) ** 2


def volume(depth) :
    return (area(depth) * (x + depth) - area(0) * x) / 3


q_sum = 0
q_life = 0
q_dam = 0

for month in range(MONTHS_IN_YEAR) :
    temperature = TEMPERATURE[month]
    evapor = PRE_CONST * math.exp(-1 / temperature) / temperature
    qq = q_sum - q_dam - q_life

# dV=x-yV
# -> V=exp(-y*t+const1)+x*t+const2

# print(volume(60.35))
# print(area(60.35))
# vol=29686054
# tmp=length(LAKE_DEPTH)
# he=tmp*SIDE_SLOPE/2
# h=3*vol/area(LAKE_DEPTH)
# print(h)

print(volume(208))