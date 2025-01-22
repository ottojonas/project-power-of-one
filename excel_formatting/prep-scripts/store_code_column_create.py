import pandas as pd

# store codes
store_codes = ["SF", "RP", "FH"]

file_path = "excel_formatting/excel-sheets/modified_storelist3.xlsx"
df = pd.read_excel(file_path)


# function to extract store codes
def extract_and_remove_store_codes(city):
    codes_found = []
    for code in store_codes:
        if code in city:
            codes_found.append(code)
            city = city.replace(code, "").strip()
    return codes_found, city


# apply the function to the 'city' column
df["store_codes"], df["city"] = zip(*df["city"].apply(extract_and_remove_store_codes))

# split the store_codes into separate columns
store_code_df = df["store_codes"].apply(pd.Series)
store_code_df.columns = [f"store_code_{i+1}" for i in store_code_df.columns]

# concatenate the new store code columns with the original DataFrame
df = pd.concat([df, store_code_df], axis=1).drop(columns=["store_codes"])

# save output file
output_file_path = "excel_formatting/excel-sheets/modified_storelist4.xlsx"
df.to_excel(output_file_path, index=False)
