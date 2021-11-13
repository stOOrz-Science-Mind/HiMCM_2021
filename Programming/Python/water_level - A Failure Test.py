import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data3.csv'

with open(filename) as f :
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    dates = []
    level = []

    for year in range(1935, 2022) :
        for month in range(1,13) :
            dates.append(f"{year}/{month}")
    # for j in range(12):
    #     for i in range(87):
    #         level.append(f(i,j))

    for row in reader :
        for i in range(1, 88) :
            print(row[i].strip())
            tmp = float((row[i].strip()))
            level.append(tmp)
    # print(level)
    # print(dates)
fig, ax = plt.subplots()
# ax.plot(dates, level, c = 'blue')

print(float('123.12'))