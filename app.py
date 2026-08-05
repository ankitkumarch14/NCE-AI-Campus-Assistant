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
st.markdown("""
<style>

.main{
background:#f5f7fb;
}

.hero{
background:linear-gradient(135deg,#004aad,#00b4d8);
padding:35px;
border-radius:20px;
color:white;
text-align:center;
margin-bottom:20px;
box-shadow:0px 10px 30px rgba(0,0,0,.2);
}

.card{
background:white;
padding:18px;
border-radius:15px;
box-shadow:0px 5px 15px rgba(0,0,0,.1);
margin-top:10px;
}

.stButton>button{
background:#004aad;
color:white;
border-radius:10px;
height:50px;
width:100%;
font-size:18px;
border:none;
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🎓 Nalanda College of Engineering</h1>
<h3>NCE AI Campus Assistant</h3>

<p>
Admission • Departments • Placement • Hostel • Faculty • Library • AI Help
</p>

</div>
""",unsafe_allow_html=True)

# Title
st.title("🎓 Nalanda College of Engineering, Chandi")

st.markdown("### 🤖 NCE AI Campus Assistant")

# Hero Image
st.image("campus1.jpg",use_container_width=True)

st.markdown("---")
st.markdown("## 🚀 Quick Access")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.button("🎓 Admission")

with c2:
    st.button("🏢 Departments")

with c3:
    st.button("💼 Placement")

with c4:
    st.button("🤖 Ask AI")

c5,c6,c7,c8=st.columns(4)

with c5:
    st.button("🏨 Hostel")

with c6:
    st.button("📚 Library")

with c7:
    st.button("👨‍🏫 Faculty")

with c8:
    st.button("📞 Contact")
    st.markdown("## 🚀 Quick Navigation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("🏫 About")

with col2:
    st.button("🏢 Departments")

with col3:
    st.button("💼 Placement")

with col4:
    st.button("🤖 Ask AI")

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.button("🏨 Hostel")

with col6:
    st.button("📚 Library")

with col7:
    st.button("👨‍🏫 Faculty")

with col8:
    st.button("📞 Contact")

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

st.markdown("## ⭐ Why Choose NCE?")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("✅ AICTE Approved")

with col2:
    st.success("🎓 BEU Affiliated")

with col3:
    st.success("📶 Wi-Fi Campus")

st.markdown("---")

st.subheader("🤖 Ask NCE AI")

question = st.text_input("Ask anything about NCE")

if st.button("Search"):
    q = question.lower().strip()

    if q in college_data["faq"]:
        st.success(college_data["faq"][q])
    else:
        st.warning("Sorry! Answer not available yet.")
