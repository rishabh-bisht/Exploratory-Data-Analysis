import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df = pd.read_csv(r"C:\Users\risha\Downloads\SampleSuperstore.csv")
print(df.head(10))

print(df.shape)

df = df.drop(["Country"], axis = 1)
print(df.head())

print(df.isnull().sum())

plt.figure(figsize=(20,10))
plt.bar('Sub-Category','Category', data = df)
plt.show()
plt.figure(figsize=(20,10))
pd.crosstab(df["Quantity"],df["Category"],df["Profit"],aggfunc='sum').plot(kind="bar",stacked=True)
plt.show()
plt.figure(figsize=(20,10))
df['Sub-Category'].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()
sns.scatterplot("Sales",'Profit',data=df)
plt.show()
plt.figure(figsize=(20,10))
sns.pairplot(df,hue='Sub-Category')
plt.show()
