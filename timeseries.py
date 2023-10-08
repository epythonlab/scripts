"""Time Series Analysis
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# pip install statsmodels 
from statsmodels.tsa.seasonal import seasonal_decompose

# generating sample time series data
np.random.seed(0)
time = pd.date_range(start='2022-01-01', periods=365, freq='D')
data = np.cumsum(np.random.randn(365))

# create a pandas dataframe
ts_data = pd.DataFrame({'Date':time, 'value': data})
print(ts_data)


# Decompose time series into trend, seasonal, residual components
result = seasonal_decompose(ts_data['value'], model='additive', period=30)

print(result)

# plot the original time series, tren, seasonal, and residual components
plt.figure(figsize=(10, 6))
plt.plot(ts_data['Date'], ts_data['value'], label='Original', linewidth=2)
plt.plot(ts_data['Date'], result.trend, label='Trend', linewidth=2)
plt.plot(ts_data['Date'], result.seasonal, label='Seasonal', linewidth=2)
plt.plot(ts_data['Date'], result.resid, label='Residual', linewidth=2)
plt.title('Time Series Analaysis')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.savefig('ts.png')
plt.show()