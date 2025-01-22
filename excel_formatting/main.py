import pandas as pd

# load excel file
file_path = "excel_formatting/excel-sheets/modified_storelist.xlsx"
df = pd.read_excel(file_path)

df[["numbers", "product", "city"]] = df.iloc[:, 0].str.extract(
    r"(\d+)\s+(Blackthorn Sea Salt Flks)\s+(.+)"
)

# save to new excel file
output_file_path = "excel_formatting/excel-sheets/modified_storelist2.xlsx"
df.to_excel(output_file_path, index=False)
