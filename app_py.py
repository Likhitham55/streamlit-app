import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit Assignment App", layout="wide")

st.title("🚀 Streamlit Hands-on Assignment App")

# -------------------------------------------
# 1️: Display Name, Role and Skills
# -------------------------------------------
st.header(" My Profile")

st.write("Name: Likhitha")
st.write("Role: Aspiring Data Scientist")
st.write("Skills: Python, SQL, Machine Learning, Streamlit")

st.divider()

# -------------------------------------------
# 2️: User Input with Button
# -------------------------------------------
st.header(" User Input Section")

name = st.text_input("Enter your Name")
age = st.number_input("Enter your Age", min_value=1, max_value=100)

if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old.")

st.divider()

# -------------------------------------------
# 3️: Checkbox Show/Hide Text
# -------------------------------------------
st.header(" Checkbox Example")

if st.checkbox("Show Welcome Message"):
    st.write("Welcome to Streamlit Learning!")

st.divider()

# -------------------------------------------
# 4️: Selectbox Programming Language
# -------------------------------------------
st.header(" Select Programming Language")

language = st.selectbox(
    "Choose a Programming Language",
    ["Python", "Java", "C++", "JavaScript"]
)

st.write(f"You selected: {language}")

st.divider()

# -------------------------------------------
# 5️: Simple Counter (No Session State)
# -------------------------------------------
st.header(" Simple Counter (No Session State)")

count = 0
if st.button("Increase Counter"):
    count += 1

st.write("Counter Value:", count)

st.divider()

# -------------------------------------------
# 6️: Display DataFrame
# -------------------------------------------
st.header(" Display DataFrame")

data = {
    "Name": ["Asha", "Ravi", "Kiran"],
    "Age": [23, 25, 22],
    "City": ["Bangalore", "Chennai", "Hyderabad"]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.divider()

# -------------------------------------------
# 7️: Upload CSV & Display
# -------------------------------------------
st.header(" Upload CSV File")

file = st.file_uploader("Upload a CSV file", type="csv")

if file is not None:
    uploaded_df = pd.read_csv(file)
    st.write("Uploaded Data")
    st.dataframe(uploaded_df)

st.divider()

# -------------------------------------------
# 8️: Display Image
# -------------------------------------------
st.header(" Display Image")

st.image("image.jpg", caption="Sample Image", use_column_width=True)

st.divider()

# -------------------------------------------
# 9️: Sidebar Course Menu
# -------------------------------------------
st.sidebar.title("📚 Courses")

course = st.sidebar.selectbox(
    "Choose a Course",
    ["Data Science", "Full Stack Python", "Full Stack Java", "Oracle"]
)

st.sidebar.success(f"You selected {course}")

st.divider()

# -------------------------------------------
# 10: Success Message Button
# -------------------------------------------
st.header(" Success Message Example")

if st.button("Click for Success"):
    st.success("Operation Completed Successfully!")

st.divider()