#series = single column=1d array
#dataframe = 2 or more series put together = numpy 2d array
#panel data = 2 or more dataframe put together =numpy 3d array

import pandas as pd
# enr=pd.Series([1,2,3,4,5,6],index=['A','B','C','D','E','F'])
# print(enr)
data=pd.DataFrame([['A','B','C'],[10,12,9]]).T
print(data)
# df=pd.read_csv(r"C:\Users\sansk\Downloads\MER_T07_02A-2020-02-03.csv")
# print(df)

data=pd.read_csv(r"C:\Users\sansk\OneDrive\Documents\Boston.csv")
pd.set_option('display.max_column',2)
pd.set_option('display.max_rows',2)
print(data.info())
print(data.shape)
print(data.shape[0])
print(list(data.columns))
print(data['INDUS '])
print(data.describe().T)
print(data.describe(percentiles=[0.3,0.5]))
print(data.describe(include=[int]))