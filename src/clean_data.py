import json
import pandas as pd
import os

# import env variables
with open("config.json", "r") as f:
    config = json.load(f)

# delete whitespace while importing raw data
df = pd.read_csv(filepath_or_buffer=config["raw_data"], skipinitialspace=True)

# write to clean data folder
# check if data folder exists
data_dir = os.path.dirname(config["clean_data"])
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

# write to data folder
clean_data_pth = os.path.join(config["clean_data"])
df.to_csv(path_or_buf=clean_data_pth, index=False)
