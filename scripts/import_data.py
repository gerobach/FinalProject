import pandas as pd

# Load XPT file
df = pd.read_sas("data/raw/DEMO_L.xpt")


# First 5 rows
print(df.head())

# Structure
print(df.info())

# Column names
print(df.columns)