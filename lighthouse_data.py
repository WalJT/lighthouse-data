import pandas as pd

# Read all tables from the Wikipedia's page on Lighthouses in Ireland
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_lighthouses_in_Ireland")

# print(tables)
# Looks like tables 0, 1 and 2 are lighthouses maintained by Commissioners of Irish Lights,
# lighthouses maintained by other Irish marine authorities, and decomissioned lightouses respectively

# Select the tables for the corresponding data
coil_lighthouse_df = tables[0]
other_lightouse_df = tables[1]
decomissioned_lighouse_df = tables[2]

print(decomissioned_lighouse_df.columns)