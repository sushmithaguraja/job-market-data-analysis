import streamlit as st
import matplotlib.pyplot as plt

from analysis import (
    load_data,
    top_skills_by_role,
    demand_by_location,
    salary_distribution
)

st.set_page_config(page_title="Job Market Insights", layout="wide")

st.title("📊 Job Market Insights Dashboard")

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
role = st.sidebar.text_input("Job Role", "Data Scientist")

# ---- Top Skills ----
st.subheader(f"Top Skills for {role}")
skills = top_skills_by_role(df, role)

fig1, ax1 = plt.subplots()
skills.plot(kind="barh", ax=ax1)
ax1.set_xlabel("Count")
st.pyplot(fig1)

# ---- Demand by Location ----
st.subheader("Top Hiring Locations")
locations = demand_by_location(df)

fig2, ax2 = plt.subplots()
locations.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Job Count")
st.pyplot(fig2)

# ---- Salary Distribution ----
salary = salary_distribution(df)
if salary is not None:
    st.subheader("Salary Distribution")
    fig3, ax3 = plt.subplots()
    ax3.hist(salary, bins=20)
    ax3.set_xlabel("Salary")
    st.pyplot(fig3)
