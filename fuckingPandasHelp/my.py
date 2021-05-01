import pandas as pd
import csv
#from sklearn.model_selection import train_test_split

df = pd.read_csv('coords.csv', engine='python',header=0,sep='::')
#print(df[df["class"]=='happy'])
#print(list(df.columns))
#cities = df['class;']
#fd = df['class'].index.to_list()
#print(fd)
fd = df[df['class']].head()
print(fd)