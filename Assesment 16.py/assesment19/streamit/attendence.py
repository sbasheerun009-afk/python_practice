import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page Configuration
st.set_page_config(
    page_title="Attendance Management System",
    page_icon="📋",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stButton>button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
}
h1 {
    text-align: center;
    color: #1E3A8A;
}
</style>
""", unsafe_allow_html=True)

st.title("📋 Attendance Management System")

file_name = "attendance.csv"

# Create CSV if not exists
if not os.path.exists(file_name):
    df = pd.DataFrame(
        columns=["Name", "Date", "In Time", "Out Time", "Working Hours"]
    )
    df.to_csv(file_name, index=False)

# Input Section
st.subheader("Mark Attendance")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Employee Name")

with col2:
    date = st.date_input("Date")

col3, col4 = st.columns(2)

with col3:
    in_time = st.time_input("In Time")

with col4:
    out_time = st.time_input("Out Time")

# Save Attendance
if st.button("Save Attendance"):
    if name:

        in_datetime = datetime.combine(date, in_time)
        out_datetime = datetime.combine(date, out_time)

        hours = round(
            (out_datetime - in_datetime).total_seconds() / 3600, 2
        )

        new_record = pd.DataFrame({
            "Name": [name],
            "Date": [date],
            "In Time": [in_time],
            "Out Time": [out_time],
            "Working Hours": [hours]
        })

        existing_df = pd.read_csv(file_name)
        updated_df = pd.concat(
            [existing_df, new_record],
            ignore_index=True
        )

        updated_df.to_csv(file_name, index=False)

        st.success("Attendance Saved Successfully ✅")

    else:
        st.error("Please Enter Employee Name")

# Display Attendance
st.subheader("Attendance Records")

attendance_df = pd.read_csv(file_name)

st.dataframe(
    attendance_df,
    use_container_width=True
)

# Statistics
if not attendance_df.empty:
    st.subheader("Attendance Summary")

    total_records = len(attendance_df)
    total_employees = attendance_df["Name"].nunique()

    c1, c2 = st.columns(2)

    c1.metric("Total Records", total_records)
    c2.metric("Employees", total_employees)

# Download Button
st.subheader("Download Attendance Sheet")

with open(file_name, "rb") as file:
    st.download_button(
        label="📥 Download CSV",
        data=file,
        file_name="attendance_sheet.csv",
        mime="text/csv"
    )

# Search Employee
st.subheader("Search Employee")

search = st.text_input("Enter Employee Name")

if search:
    result = attendance_df[
        attendance_df["Name"].str.contains(search, case=False, na=False)
    ]

    st.dataframe(result, use_container_width=True)