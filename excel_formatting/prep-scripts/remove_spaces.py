import pandas as pd

# load the Excel file
file_path = "excel_formatting/excel-sheets/mands_storelist.xlsx"
df = pd.read_excel(file_path)

# remove all spaces from the 'city' column
df["city"] = df["city"].str.replace(" ", "")

# save the modified DataFrame to a new Excel file
output_file_path = "excel_formatting/excel-sheets/modified_mands_storelist.xlsx"
df.to_excel(output_file_path, index=False)
