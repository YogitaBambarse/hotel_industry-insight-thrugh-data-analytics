import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hotel Industry Analytics", layout="wide")

# Load data
df = pd.read_csv("hotel_data.csv")

# Sidebar filters
st.sidebar.header("🔍 Filters")

month = st.sidebar.multiselect(
    "Month", df["Month"].unique(), default=df["Month"].unique()
)

room = st.sidebar.multiselect(
    "Room Type", df["Room_Type"].unique(), default=df["Room_Type"].unique()
)

source = st.sidebar.multiselect(
    "Booking Source", df["Booking_Source"].unique(), default=df["Booking_Source"].unique()
)

customer = st.sidebar.multiselect(
    "Customer Type", df["Customer_Type"].unique(), default=df["Customer_Type"].unique()
)

filtered = df[
    (df["Month"].isin(month)) &
    (df["Room_Type"].isin(room)) &
    (df["Booking_Source"].isin(source)) &
    (df["Customer_Type"].isin(customer))
]

# Title
st.title("🏨 Hotel Industry Analytics Dashboard")
st.caption("Python + Streamlit Data Analytics Website")

# KPIs
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("📦 Total Bookings", filtered["Booking_ID"].nunique())
c2.metric("💰 Total Revenue", f"₹{filtered['Revenue'].sum():,.0f}")
c3.metric("🛏 Avg Stay Days", f"{filtered['Stay_Days'].mean():.1f}")
c4.metric("🏨 Avg Occupancy", f"{filtered['Occupancy'].mean():.1f}%")
c5.metric("⭐ Avg Rating", f"{filtered['Rating'].mean():.2f}")

st.divider()

# Revenue chart (Streamlit built-in)
st.subheader("📈 Revenue by Month")
rev_month = filtered.groupby("Month")["Revenue"].sum()
st.line_chart(rev_month)

st.divider()

# Customer Type chart
st.subheader("👥 Revenue by Customer Type")
cust_rev = filtered.groupby("Customer_Type")["Revenue"].sum()
st.bar_chart(cust_rev)

st.divider()

# Insights
st.subheader("📌 Business Insights")
st.write("""
• Corporate customers have longer stays  
• OTA bookings generate higher revenue  
• Peak months show strong revenue growth  
""")

st.caption("Developed by Yogita Bambarse")
