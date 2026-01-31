import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hotel Industry Analytics", layout="wide")

# Load dataset
df = pd.read_csv("hotel_data.csv")

# ---------- SIDEBAR ----------
st.sidebar.header("🔍 Filters")

month = st.sidebar.multiselect(
    "Select Month",
    df["Month"].unique(),
    default=df["Month"].unique()
)

room = st.sidebar.multiselect(
    "Select Room Type",
    df["Room_Type"].unique(),
    default=df["Room_Type"].unique()
)

source = st.sidebar.multiselect(
    "Select Booking Source",
    df["Booking_Source"].unique(),
    default=df["Booking_Source"].unique()
)

customer = st.sidebar.multiselect(
    "Select Customer Type",
    df["Customer_Type"].unique(),
    default=df["Customer_Type"].unique()
)

filtered_df = df[
    (df["Month"].isin(month)) &
    (df["Room_Type"].isin(room)) &
    (df["Booking_Source"].isin(source)) &
    (df["Customer_Type"].isin(customer))
]

# ---------- TITLE ----------
st.title("🏨 Hotel Industry Analytics Dashboard")
st.caption("Python + Streamlit Data Analytics Website")

# ---------- KPIs ----------
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("📦 Total Bookings", filtered_df["Booking_ID"].nunique())
c2.metric("💰 Total Revenue", f"₹{filtered_df['Revenue'].sum():,.0f}")
c3.metric("🛏 Avg Stay Days", f"{filtered_df['Stay_Days'].mean():.1f}")
c4.metric("🏨 Avg Occupancy", f"{filtered_df['Occupancy'].mean():.1f}%")
c5.metric("⭐ Avg Rating", f"{filtered_df['Rating'].mean():.2f}")

st.divider()

# ---------- CHARTS ----------
st.subheader("📈 Revenue by Month")
revenue_month = filtered_df.groupby("Month")["Revenue"].sum()
st.line_chart(revenue_month)

st.subheader("👥 Revenue by Customer Type")
cust_rev = filtered_df.groupby("Customer_Type")["Revenue"].sum()
st.bar_chart(cust_rev)

st.divider()

# ---------- INSIGHTS ----------
st.subheader("📌 Business Insights")
st.write("""
• Corporate customers show longer stay duration  
• OTA booking source contributes higher revenue  
• Peak months significantly improve hotel performance  
""")

st.caption("Developed by Yogita Bambarse")
