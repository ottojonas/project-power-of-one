import pandas as pd

# Load the Excel file
file_path = "excel_formatting/excel-sheets/modified_mands_storelist.xlsx"
df = pd.read_excel(file_path)

# Add ',GB' to the 'location' column
df["location"] = df["location"] + ",GB"

# Save the modified DataFrame to a new Excel file
output_file_path = (
    "excel_formatting/excel-sheets/modified_mands_storelist_with_gb_and_no_space.xlsx"
)
df.to_excel(output_file_path, index=False)
