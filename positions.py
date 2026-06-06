import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Positions")

df = pd.read_csv("Positions.csv")
df["SOD Pos"] = pd.to_numeric(df["SOD Pos"].astype(str).str.replace(",", ""), errors="coerce")

fig = px.bar(df, x="FNYSym", y="SOD Pos", title="SOD Position by Symbol")
st.plotly_chart(fig, use_container_width=True)
