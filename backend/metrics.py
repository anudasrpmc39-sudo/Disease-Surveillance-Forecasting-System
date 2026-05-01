def calculate_incidence(df, population_df):
    df = df.merge(population_df, on="area", how="left")
    df["incidence"] = (df["cases"] / df["population"]) * 100000
    return df

def calculate_cfr(df, deaths_df):
    df = df.merge(deaths_df, on=["area", "date"], how="left")
    df["cfr"] = (df["deaths"] / df["cases"]) * 100
    return df
