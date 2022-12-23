import csv
import pandas as pd

df = pd.read_csv("final_stars.csv")
print(df.columns)

del df ["Luminosity"]
del df ["Star_name.1"]
del df ["Distance.1"]
del df ["Mass.1"]
del df ["Radius.1"]
del df["Unnamed: 6"]
del df["Unnamed: 0"]
print(df.columns)
df.to_csv("main.csv")