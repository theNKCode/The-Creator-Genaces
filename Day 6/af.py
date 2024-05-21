import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('C:/Users/nikhi/Downloads/SalaryData.csv')
print(df)

X= df['YearsExperience'].values.reshape(-1,1)
y= df['Salary']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print(y_pred)


plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()