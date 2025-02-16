import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Database connection
conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS portfolio (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT,
                    revenue REAL,
                    ebitda REAL,
                    cash_flow REAL,
                    debt_levels REAL,
                    forecast_variance REAL)''')
conn.commit()

# Load data
query = "SELECT * FROM portfolio"
df = pd.read_sql(query, conn)

# Streamlit UI
st.title("Portfolio Monitoring Dashboard")
st.sidebar.header("Filters")
company_filter = st.sidebar.multiselect("Select Company", df["company"].unique())

# Apply filters
if company_filter:
    df = df[df["company"].isin(company_filter)]

# KPIs Display
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${df['revenue'].sum():,.2f}")
col2.metric("Total EBITDA", f"${df['ebitda'].sum():,.2f}")
col3.metric("Total Cash Flow", f"${df['cash_flow'].sum():,.2f}")
col4.metric("Total Debt Levels", f"${df['debt_levels'].sum():,.2f}")

# Visualization
st.subheader("Revenue Trend")
fig = px.bar(df, x='company', y='revenue', title='Revenue by Company')
st.plotly_chart(fig)

st.subheader("EBITDA vs Cash Flow")
fig2 = px.scatter(df, x='ebitda', y='cash_flow', color='company', title='EBITDA vs Cash Flow')
st.plotly_chart(fig2)

# Alerts for Underperformance
st.subheader("Alerts")
alerts = df[df['forecast_variance'] < 0]
st.dataframe(alerts)

# Close DB connection
conn.close()
