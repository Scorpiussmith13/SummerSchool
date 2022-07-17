import pandas as pd
import csv

header  = ['Rule_No','Size 4', 'Size 5', 'Size 6', 'Size 7', 'Size 8', 'Size 9', 'Size 10', 'Size 11', 'Size 12','Overall' ]
columns = ["Rule_no"]


df = pd.read_csv("result_for_latticeSize4.csv", usecols=columns)
df.to_csv('Results.csv', mode='a', sep='\t', encoding='utf-8', index=False, header=False)
    




