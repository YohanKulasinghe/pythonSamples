import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import xlrd

loc = ("FIT16.xlsx")
indexes = []
names = []
checkDigit = input("Please enter the last digit: ")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    if(sheet.cell_value(i, 1)[5:6] == checkDigit):
        indexes.append(sheet.cell_value(i,1))
        names.append(sheet.cell_value(i,2))
    
print("\n There are",len(names)," students having ",checkDigit," as last digit of their index\n")
for i, n in zip(indexes, names):
    print("{} = {}".format(i,n))

