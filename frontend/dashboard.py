import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("Disease Surveillance Dashboard")

data = requests.get("http://localhost:8000/data").json()
df = pd.DataFrame(data)

st.subheader("Daily Cases")
fig = px.line(df, x="date", y="cases", color="disease")
st.plotly_chart(fig)

forecast_data = requests.get("http://localhost:8000/forecast").json()
forecast_df = pd.DataFrame(forecast_data)

st.subheader("Forecast")
fig2 = px.line(forecast_df, x="ds", y="yhat")
st.plotly_chart(fig2)
