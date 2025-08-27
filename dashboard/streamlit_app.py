import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
import plotly.express as px

# DATABASE
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL = "postgresql+psycopg2://fraud_db_jpjc_user:TJGUo8HE9lVAVWb2cPdwZEEmnbWZBvY5@dpg-d2mledbuibrs73bhvm90-a.frankfurt-postgres.render.com:5432/fraud_db_jpjc"

engine = create_engine(DATABASE_URL)

@st.cache_data(ttl=60)
def load_transactions():
    df = pd.read_sql("SELECT * FROM transactions ORDER BY id DESC", engine)
    df['created_at'] = pd.to_datetime(df['created_at'])
    return df

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")
st.title("💳 Fraud Detection Dashboard")

df = load_transactions()
total_tx = len(df)
total_fraud = df['is_fraud'].sum()
avg_prob = df['probability'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", total_tx)
col2.metric("Total Fraudulent", total_fraud)
col3.metric("Avg Fraud Probability", f"{avg_prob:.2f}")

st.subheader("Latest Transactions")
st.dataframe(df.tail(20))

st.subheader("Fraud Probability Over Time")
fig = px.line(df, x='created_at', y='probability', color='is_fraud',
              labels={'is_fraud':'Fraud','probability':'Probability'})
st.plotly_chart(fig, use_container_width=True)

st.subheader("Filter Transactions by Fraud Probability")
threshold = st.slider("Minimum Probability", 0.0, 1.0, 0.5, 0.01)
filtered = df[df['probability'] >= threshold]
st.dataframe(filtered)
