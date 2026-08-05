import streamlit as st

st.set_page_config(page_title="NCE Home", page_icon="🏫", layout="wide")

# Logo
st.image("../logo.jpg", width=120)

# Title
st.title("🎓 Nalanda College of Engineering, Chandi")

st.markdown("### Welcome to NCE AI Campus Assistant")

# Hero Banner
st.image("../image/campus1.jpg", use_container_width=True)

st.markdown("---")

# Quick Info
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Established", "2008")

with col2:
    st.metric("Courses", "B.Tech & M.Tech")

with col3:
    st.metric("Hostels", "4")

with col4:
    st.metric("Departments", "6")

st.markdown("---")

st.subheader("🏫 About NCE")

st.write("""
Nalanda College of Engineering (NCE), Chandi is an AICTE-approved engineering college
affiliated with Bihar Engineering University (BEU). The college offers quality technical
education with modern laboratories, library, hostels, Wi-Fi campus and experienced faculty.
""")