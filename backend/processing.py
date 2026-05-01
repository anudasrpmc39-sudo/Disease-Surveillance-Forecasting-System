import pandas as pd

def process_data(raw_data):
    rows = raw_data.get("rows", [])
    
    df = pd.DataFrame(rows, columns=["dx", "pe", "ou", "value"])

    df.rename(columns={
        "dx": "disease",
        "pe": "date",
        "ou": "area",
        "value": "cases"
    }, inplace=True)

    df["cases"] = df["cases"].astype(int)

    return df
