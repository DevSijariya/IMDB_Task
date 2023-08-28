import pandas as pd
data=pd.read_csv(r"D:\lnb data science course\pandas\diabetes.csv")
print(data.describe(percentiles=[0.3,0.5,1.]))
print(data.describe(include=[int]))
s=data