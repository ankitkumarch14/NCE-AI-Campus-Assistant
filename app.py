import streamlit as st
import json

st.set_page_config(
    page_title="NCE AI Campus Assistant",
    page_icon="🎓",
    layout="wide"
)

# Load Data
with open("college_data.json", "r") as file:
    college_data = json.load(file)

# Logo
st.image("logo.jpg", width=120)

# Title
st.title("🎓 Nalanda College of Engineering, Chandi")

st.markdown("### 🤖 NCE AI Campus Assistant")

# Hero Image

st.markdown("---")

# Quick Facts
col1, col2, col3, col4 = st.columns(4)

col1.metric("🏛 Established", "2008")
col2.metric("🎓 Courses", "B.Tech | M.Tech")
col3.metric("🏨 Hostels", "4")
col4.metric("🏫 Departments", "6+")

st.markdown("---")

st.subheader("📖 About College")

st.write("""
Nalanda College of Engineering (NCE), Chandi is one of the premier government engineering colleges of Bihar.

It is approved by AICTE and affiliated to Bihar Engineering University (BEU).

The college offers quality technical education with modern laboratories, smart classrooms, central library, Wi-Fi campus, hostels and experienced faculty.
""")

st.markdown("---")

st.subheader("🤖 Ask NCE AI")

question = st.text_input("Ask anything about NCE")

if st.button("Search"):
    q = question.lower().strip()

    if q in college_data["faq"]:
        st.success(college_data["faq"][q])
    else:
        st.warning("Sorry! Answer not available yet.")
