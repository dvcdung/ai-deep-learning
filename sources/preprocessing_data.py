import os

data_file = 'data/houses.csv'

# Saved for later use
def mkdir_if_not_exists(path):
    if not isinstance(path, str):
        path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)

mkdir_if_not_exists('data')

# with open(data_file, 'w') as f:
#     f.write('NumRoom,Alley,Price\n')
#     f.write('3,Pave,120\n')
#     f.write('NA,Del,140\n')
#     f.write('4,NA,167\n')

import pandas as pd

data = pd.read_csv(data_file)
print(data)
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]

# 2 methods are commonly used for handling missing data
## imputation (quy buộc/ áp đặt) NaN is changed to mean
inputs = inputs.fillna(inputs.mean(numeric_only=True))
print(inputs)
## deletion

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)

from mxnet import np, npx
# Convert to ndarray ------------------------------------------< JOHN TAG
X, y = np.array(inputs.values), np.array(outputs.values)
print (X, y)