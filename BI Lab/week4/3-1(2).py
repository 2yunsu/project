import pandas as pd
data=pd.read_csv('C:/Users/User/OneDrive/문서/Pycharm/BI Lab/week4/bee_data.csv')
sorted_data=data.sort_values(by='Lost Colonies',ascending=False)
top10=sorted_data.iloc[:10]
print(top10)