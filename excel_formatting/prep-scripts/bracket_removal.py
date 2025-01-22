import pandas as pd

# load excel file path
file_path = "excel_formatting/storelist.xlsx"
df = pd.read_excel(file_path)

# remove brackets from all string columns
df = df.applymap(
    lambda x: x.replace("(", "").replace(")", "") if isinstance(x, str) else x
)

# save to new output file
output_file_path = "excel_formatting/modified_storelist.xlsx"
df.to_excel(output_file_path, index=False)
