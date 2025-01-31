import pandas as pd 
original_path = 'distance_tracking/excel/sales_data.xlsx'  
df = pd.read_excel(original_path)
df = df.applymap(
    lambda x: x.replace("GRAD2", 'KA8 8AE').replace("SH2", 'KA8 8AE').replace("AYR2", 'KA8 8AE').replace("SGS", 'PA3 4JA').replace("AST", 'WA7 1PW').replace("AB", 'WA7 1PW').replace("IMM", "DN40 2QQ").replace("ROS", "KY11 2YD").replace("KGV", "G51 42D").replace("RUN", "WA7 4UY") if isinstance(x, str) else x
)

updated_file_path = 'distance_tracking/excel/sales_data_modified.xlsx'
df.to_excel(updated_file_path, index = False)



