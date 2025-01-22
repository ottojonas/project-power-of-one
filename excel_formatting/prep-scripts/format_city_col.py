import pandas as pd

# load the Excel file
file_path = "excel_formatting/excel-sheets/modified_storelist2.xlsx"
df = pd.read_excel(file_path)

# remove '/' from the 'city' column
df["city"] = df["city"].str.replace("/", "")

# save the modified DataFrame to a new Excel file
output_file_path = "excel_formatting/excel-sheets/modified_storelist3.xlsx"
df.to_excel(output_file_path, index=False)
