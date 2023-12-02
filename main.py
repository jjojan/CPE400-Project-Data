from os import name
import numpy as np
import pandas as pand
import math

file_list = ['Instagram_Android_Data.csv','Instagram_Android_Data2.csv','Instagram_Android_Data3.csv','Instagram_Android_Data4.csv','Instagram_Android_Data5.csv',
             'Instagram_Android_Data6.csv','Instagram_Android_Data7.csv','Instagram_Android_Data8.csv','Instagram_Android_Data9.csv','Instagram_Android_Data10.csv']

dataFrame = pand.DataFrame(pand.read_csv(file_list[0]))

for i in range(1,len(file_list)):
    data = pand.DataFrame(pand.read_csv(file_list[i]))
    dataFrame = pand.concat([dataFrame,data])

print(dataFrame)
    

proto = dataFrame.groupby(['Proto'])['Proto'].count().reset_index(name='Count').sort_values(['Count'],ascending = False)
print(proto)

dataFrame['totalTime'] = dataFrame.LastSeen - dataFrame.FirstSeen

timeFrame = dataFrame.sort_values(by='totalTime', ascending = False)
print(timeFrame[['Proto','totalTime']])

