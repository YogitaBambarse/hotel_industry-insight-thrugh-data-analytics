import streamlit as st
import pandas as pd
st.line_chart(revenue_month)

st.set_page_config(page_title="Hotel Industry Analytics", layout="wide")

# Load dataset
df = pd.read_csv("hotel_data.csv")

# ---------- SIDEBAR FILTERS ----------
st.sidebar.header("🔍 Filters")

months = st.sidebar.multiselect(
    "Select Month", df["Month"].unique(), default=df["Month"].unique()
)

room_type = st.sidebar.multiselect(
    "Select Room Type", df["Room_Type"].unique(), default=df["Room_Type"].unique()
)

booking_source = st.sidebar.multiselect(
    "Select Booking Source", df["Booking_Source"].unique(), default=df["Booking_Source"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select Customer Type", df["Customer_Type"].unique(), default=df["Customer_Type"].unique()
)

filtered_df = df[
    (df["Month"].isin(months)) &
    (df["Room_Type"].isin(room_type)) &
    (df["Booking_Source"].isin(booking_source)) &
    (df["Customer_Type"].isin(customer_type))
]

# ---------- TITLE ----------
st.title("🏨 Hotel Industry Analytics Dashboard")
st.caption("Python + Streamlit Data Analytics Project")

# ---------- KPI METRICS ----------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("📦 Total Bookings", filtered_df["Booking_ID"].nunique())
col2.metric("💰 Total Revenue", f"₹{filtered_df['Revenue'].sum():,.0f}")
col3.metric("🛏 Avg Stay (Days)", f"{filtered_df['Stay_Days'].mean():.1f}")
col4.metric("🏨 Avg Occupancy", f"{filtered_df['Occupancy'].mean():.1f}%")
col5.metric("⭐ Avg Rating", f"{filtered_df['Rating'].mean():.2f}")

st.markdown("---")

# ---------- REVENUE BY MONTH ----------
st.subheader("📈 Revenue by Month")

revenue_month = filtered_df.groupby("Month")["Revenue"].sum()

fig, ax = plt.subplots()
ax.plot(revenue_month.index, revenue_month.values, marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title("Monthly Revenue Trend")

st.pyplot(fig)

# ---------- CUSTOMER TYPE ANALYSIS ----------
st.subheader("👥 Customer Type vs Revenue")

cust_rev = filtered_df.groupby("Customer_Type")["Revenue"].sum()

fig2, ax2 = plt.subplots()
ax2.bar(cust_rev.index, cust_rev.values)
ax2.set_xlabel("Customer Type")
ax2.set_ylabel("Revenue")

st.pyplot(fig2)

# ---------- BUSINESS INSIGHTS ----------
st.markdown("---")
st.subheader("📌 Business Insights")

st.markdown("""
- 💼 Corporate customers have higher average stay duration.
- 💰 OTA bookings generate higher total revenue.
- 🛏 Longer stays contribute significantly to revenue growth.
""")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Developed by Yogita Bambarse | Hotel Industry Analytics Website")
