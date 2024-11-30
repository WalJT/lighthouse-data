import pandas as pd
import datetime

# Set the date the data was extracted. This could be handy to reference in the future.
extracted_date = datetime.date.today()
print(extracted_date)

# Read all tables from the Wikipedia's page on Lighthouses in Ireland
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_lighthouses_in_Ireland")

lighthouse_dfs = {"coil": tables[0], "other": tables[1], "decom": tables[2]}
important_cols = list()

# Extract county and name of each lighthouse
for df in lighthouse_dfs.values():
	important_cols.append(df[["County", "Name"]])
	

# Merge into a single data frame, add a couple of columns and sort by county
df_merged = pd.concat(important_cols, ignore_index=True)
df_merged["Photographed"] = "❌"
df_merged["Blog Post"] = "Link Pending"
df_merged = df_merged.sort_values(by=["County", "Name"])

# Write table to a markdown file so I can copy it to the web
with open("lighthouse_table.md", "w", encoding="utf-8") as mdfile:
	mdfile.write(df_merged.to_markdown(tablefmt="pipe", index=False))

with open("lighthouse_table.html", "w", encoding="utf-8") as htmlfile:
	htmlfile.write(df_merged.to_html(index=False))