import streamlit as st
import json

# Load college data
with open("college_data.json", "r") as file:
    college_data = json.load(file)

# Page settings
st.set_page_config(
    page_title="NCE AI Campus Assistant",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
st.sidebar.title("🎓 NCE AI Assistant")
st.sidebar.success("Nalanda College of Engineering, Chandi")
st.sidebar.info("AI-powered College Information System")

# Main Title
st.title("🎓 NCE AI Campus Assistant")

st.markdown("## Welcome to Nalanda College of Engineering, Chandi")
st.write("Ask anything about the college.")

# College Name
st.success("🏫 " + college_data["college_name"])

# Quick Information
st.markdown("---")
st.subheader("📊 Quick Facts")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🏛 Established\n\n2008")

with col2:
    st.info("🎓 Courses\n\nB.Tech | M.Tech")

with col3:
    st.info("🏫 Departments\n\n6+")
    col4, col5, col6 = st.columns(3)

with col4:
    st.info("🏠 Hostels\n\n4")

with col5:
    st.info("📚 Library\n\nWi-Fi & Computers")

with col6:
    st.info("🧪 Engineering Labs\n\nAvailable")

# Search Box
question = st.text_input("🔍 Ask your question")

# Ask Button
if st.button("Ask"):
    q = question.lower().strip()

    if q in college_data["faq"]:
        st.success(college_data["faq"][q])
    else:
        st.error("❌ Sorry! I don't know the answer to this question yet.")
