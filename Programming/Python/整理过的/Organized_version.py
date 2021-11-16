import math
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line, Page
from pyecharts.faker import Faker
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve, nsolve, Symbol
import sympy

KEV = 273.15
MONTHS_IN_YEAR = 12

SIDE_SLOPE = 0.8902 * 2
LAKE_DEPTH = 162
SURFACE_ELEVATION = 375
BOTTOM_TO_SEA = SURFACE_ELEVATION - LAKE_DEPTH

LENGTH_TOP = math.sqrt(640) * 1000
LENGTH_BOTTOM = LENGTH_TOP - (2 * LAKE_DEPTH) / SIDE_SLOPE

HEIGHT_NEEDED_TO_EXPAND_TO_A_PYRAMID = LAKE_DEPTH * LENGTH_BOTTOM / (LENGTH_TOP - LENGTH_BOTTOM)
# 补成一个圆锥形

# print(HEIGHT_NEEDED_TO_EXPAND_TO_A_PYRAMID)
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
    return (area(depth) * (HEIGHT_NEEDED_TO_EXPAND_TO_A_PYRAMID + depth) - area(
        0) * HEIGHT_NEEDED_TO_EXPAND_TO_A_PYRAMID) / 3


# def volume_to_depth(volume) :
#     depth = Symbol('depth')
#     equasion = volume(depth)
#     # try :
#     output = nsolve(equasion, depth, volume)
#     # except :
#     #     output = "ERROR!"
#     return output


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

x1 = Symbol('x1')
x2 = Symbol('x2')
f1 = 3 * x1 ** 2 - 2 * x2 ** 2 - 1
f2 = x1 ** 2 - 2 * x1 + x2 ** 2 + 2 * x2 - 8
print(nsolve((f1, f2), (x1, x2), (-1, 1)))
