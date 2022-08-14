import pandas as pd
import numpy as np
#import openpyxl

df = pd.read_excel(r"C:\\Users\\VikasJadaun\\Documents\\sheet.xlsx", engine='openpyxl')

#print(df)
df.to_csv(r"E:\\new.csv")
headers=['','ticker', 'eps', 'revenue', 'price', 'people']
df.columns=headers
#print(df)
df1=df.replace('not available',np.NaN, inplace=True)
df1=df.replace('n.a.',np.NaN, inplace= True)
df1=df.replace(-1,np.NaN)
print(df1)
#defining function
def replacing(x):
    df1["people"].replace(np.NaN,x, inplace=True)
#calling it
#if np.NaN in df1["people"]
replacing("Sam Walton")
#replacing nan by mean
mean1= df1["price"].astype("float").mean(axis=0)
df1["price"].replace(np.NaN, mean1, inplace=True)
#replacing nan by frequency
rep= df1['eps'].value_counts().idxmax()
df1["eps"].replace(np.NaN, rep, inplace=True)
#replacing nan by nan
mean3= df1["revenue"].mean()
df1["revenue"].replace(np.NaN, mean3, inplace=True)
print(df1)
