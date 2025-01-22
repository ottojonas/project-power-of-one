import pandas as pd

# load excel file
file_path = "excel_formatting/storelist.xlsx"
df = pd.read_excel(file_path)

df[["numbers", "product", "city"]] = df.iloc[:, 0].str.extract(
    r"(\d+)\s+(Blackthorn Sea Salt Flakes)\s+(.+)"
)

# save to new excel file
output_file_path = "excel_formatting/modified_storelist.xlsx"
df.to_excel(output_file_path, index=False)
