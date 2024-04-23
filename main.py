import numpy as np
import pandas as pd
import json
import os

frame = {'Name':['Aditya', 'Tom', 'mathew', 'Sundar'], 'Age':[25, 29, 45, 50], 
         'Profession': ['Software Engineer(Machine Learning)', 'Actor', 'Cricketer', 'Google CEO'], 
         'Income': [500000, 700000, 80000, 200000]}


dataframe = pd.DataFrame(frame)

print(dataframe)

if not os.path.exists('Data'):
    os.mkdir('Data')

dataframe.to_csv('Data/data.csv')


