import pandas as pd
import math

def read_test_file1(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df["Test Result"] = df["Test Result"].apply(lambda x: "fail" if isinstance(x, float) and math.isnan(x) else x)
    return df.to_dict(orient='records')