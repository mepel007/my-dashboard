import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Dashboard")

# Sample data — swap in your own CSV or API later
df = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Value": [120, 145, 132, 178, 165, 190]
})

st.line_chart(df.set_index("Month"))
st.dataframe(df)