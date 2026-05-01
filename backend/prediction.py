from prophet import Prophet

def forecast_cases(df):
    df = df.groupby("date")["cases"].sum().reset_index()
    df.columns = ["ds", "y"]

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
