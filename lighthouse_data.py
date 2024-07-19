import pandas as pd

# Read all tables from the Wikipedia's page on Lighthouses in Ireland
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_lighthouses_in_Ireland")

# print(tables)
# Looks like tables 0, 1 and 2 are lighthouses maintained by Commissioners of Irish Lights,
# lighthouses maintained by other Irish marine authorities, and decomissioned lightouses respectively

# Select the tables for the corresponding data

lighthouse_dfs = {"coil": tables[0], "other": tables[1], "decom": tables[2]}

for df in lighthouse_dfs.values():
	print(df.columns)

# Columns of note:
# 	- Name at index 0
# 	- Location Coordinates at index 2
# 		- In the format of `Place Name Degrees Minuites Seconds N / Degrees Minuites Seconds W`
# 	- County at index 3

for _, row in lighthouse_dfs["coil"].iterrows():
	print(row["Location Coordinates"])