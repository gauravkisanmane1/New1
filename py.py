# import pandas as pd
# from datetime import time
# from distutils.cmd import Command as DistutilsCommand
# df = pd.read_excel('wordcraft.xlsx')
# #Display the first 10 rows
# result = df.head(10)
# print("First 10 rows of the DataFrame:")
# print(result)


a=[10,20,10,50,40,30,30]
d=[]
for ele in a:
    if a.count(ele) >1 and ele not in d:
        d.append(ele)
print(d)    