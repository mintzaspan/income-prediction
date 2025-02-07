from ucimlrepo import fetch_ucirepo
import pandas as pd
import os

# fetch dataset
census_income = fetch_ucirepo(id=20)

# data (as pandas dataframes)
X = census_income.data.features
y = census_income.data.targets

# build dataset
df = pd.merge(left=X, right=y, left_index=True, right_index=True)

# check if data folder exists
data_dir = "data"
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

# write to data folder
raw_data_pth = os.path.join(data_dir, "raw_data.csv")
df.to_csv(path_or_buf=raw_data_pth, index=False)
