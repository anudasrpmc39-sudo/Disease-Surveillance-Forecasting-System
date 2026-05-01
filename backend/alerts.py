def generate_alerts(df):
    alerts = []

    for _, row in df.iterrows():
        if row["incidence"] > 50:
            alerts.append(f"High incidence in {row['area']}")

        if row.get("cfr", 0) > 2:
            alerts.append(f"High CFR in {row['area']}")

    return alerts
