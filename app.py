import streamlit as st
import json

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="NCE AI Campus Assistant",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
with open("college_data.json","r",encoding="utf-8") as f:
    college_data=json.load(f)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

html,body,[class*="css"]{
font-family:Arial,sans-serif;
}

.main{
background:#f4f8fc;
}

.hero{
background:linear-gradient(135deg,#003366,#0077cc);
padding:35px;
border-radius:20px;
color:white;
text-align:center;
box-shadow:0px 8px 20px rgba(0,0,0,.2);
margin-bottom:25px;
}

.quick{
background:white;
padding:18px;
border-radius:15px;
box-shadow:0px 5px 15px rgba(0,0,0,.08);
text-align:center;
margin-top:10px;
}

.section{
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 5px 15px rgba(0,0,0,.08);
margin-top:20px;
margin-bottom:20px;
}

.stButton>button{
width:100%;
background:#0056b3;
color:white;
border:none;
border-radius:10px;
height:48px;
font-size:16px;
font-weight:bold;
}

.stButton>button:hover{
background:#003d80;
}

footer{
visibility:hidden;
}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# LOGO
# -----------------------------
st.image("logo.jpg",width=120)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="hero">

<h1>🎓 Nalanda College of Engineering</h1>

<h3>NCE AI Campus Assistant</h3>

<p>
AI Powered College Information System
</p>

</div>
""",unsafe_allow_html=True)

# -----------------------------
# HERO IMAGE
# -----------------------------
st.image("campus1.jpg", use_container_width=True)

st.markdown("")

# -----------------------------
# QUICK NAVIGATION
# -----------------------------
st.subheader("🚀 Quick Navigation")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.button("🎓 Admission")

with c2:
    st.button("🏢 Departments")

with c3:
    st.button("💼 Placement")

with c4:
    st.button("🤖 AI Assistant")

c5,c6,c7,c8=st.columns(4)

with c5:
    st.button("🏨 Hostel")

with c6:
    st.button("📚 Library")

with c7:
    st.button("📸 Gallery")

with c8:
    st.button("📞 Contact")

st.divider()

# -----------------------------
# QUICK FACTS
# -----------------------------
st.subheader("📊 Quick Facts")

a,b,c,d=st.columns(4)

a.metric("Established","2008")
b.metric("Departments","6+")
c.metric("Courses","B.Tech / M.Tech")
d.metric("Hostels","4")
# =====================================================
# ABOUT NCE
# =====================================================

st.markdown("""
<div class="section">
<h2>🏫 About Nalanda College of Engineering</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
Nalanda College of Engineering (NCE), Chandi is one of the premier Government Engineering Colleges of Bihar.

The college is approved by AICTE and affiliated with Bihar Engineering University (BEU), Patna.

NCE provides quality technical education through experienced faculty, modern laboratories,
digital classrooms, central library, hostel facilities, Wi-Fi campus and excellent academic environment.
""")

st.divider()

# =====================================================
# WHY CHOOSE NCE
# =====================================================

st.subheader("⭐ Why Choose NCE")

c1,c2,c3=st.columns(3)

with c1:
    st.success("✅ AICTE Approved")

with c2:
    st.success("🎓 BEU Affiliated")

with c3:
    st.success("🏛 Government Engineering College")

c4,c5,c6=st.columns(3)

with c4:
    st.info("📚 Modern Library")

with c5:
    st.info("🧪 Advanced Laboratories")

with c6:
    st.info("📶 Wi-Fi Campus")

st.divider()

# =====================================================
# DEPARTMENTS
# =====================================================

st.subheader("🏢 Departments")

d1,d2=st.columns(2)

with d1:
    st.markdown("""
### 💻 Computer Science & Engineering

- Modern Labs
- Experienced Faculty
- Programming
- Software Development
""")

    st.markdown("""
### 🤖 Artificial Intelligence & Machine Learning

- AI
- Machine Learning
- Deep Learning
- Data Science
""")

    st.markdown("""
### ⚙ Mechanical Engineering

- CAD Lab
- Manufacturing
- Thermal Engineering
""")

with d2:

    st.markdown("""
### 🏗 Civil Engineering

- Survey Lab
- Transportation
- Structural Engineering
""")

    st.markdown("""
### ⚡ Electrical Engineering

- Power System
- Machines
- Electrical Lab
""")

    st.markdown("""
### 📡 Electronics & Communication

- Digital Electronics
- Communication Lab
- Embedded Systems
""")

st.divider()

# =====================================================
# FACILITIES
# =====================================================

st.subheader("🏫 Campus Facilities")

f1,f2,f3=st.columns(3)

with f1:
    st.success("🏨 Boys & Girls Hostel")

with f2:
    st.success("📚 Central Library")

with f3:
    st.success("🚌 Transport Facility")

f4,f5,f6=st.columns(3)

with f4:
    st.success("⚽ Sports")

with f5:
    st.success("💻 Computer Labs")

with f6:
    st.success("🌐 Wi-Fi Campus")

st.divider()
# =====================================================
# ADMISSION
# =====================================================

st.subheader("🎓 Admission")

tab1, tab2 = st.tabs(["B.Tech", "M.Tech"])

with tab1:

    st.markdown("""
### B.Tech Admission

Admission is conducted through BCECE / UGEAC counselling.

Eligibility

✅ 10+2 (PCM)

✅ JEE(Main) Qualified

✅ UGEAC Counselling

Documents Required

• 10th Marksheet
• 12th Marksheet
• JEE Score Card
• Aadhar Card
• Passport Size Photo
• Migration Certificate
""")

with tab2:

    st.markdown("""
### M.Tech Admission

Admission through PG admission process.

Eligibility

✅ B.E./B.Tech Degree

Required Documents

• Graduation Marksheet
• Degree Certificate
• Identity Proof
• Passport Size Photo
""")

st.divider()

# =====================================================
# PLACEMENT
# =====================================================

st.subheader("💼 Training & Placement")

col1,col2,col3=st.columns(3)

col1.metric("Recruiters","50+")
col2.metric("Internships","Available")
col3.metric("Training","Soft Skills + Technical")

st.write("""
Training & Placement Cell helps students in internships,
campus recruitment, aptitude training,
technical interviews and personality development.
""")

st.divider()

# =====================================================
# GALLERY
# =====================================================

st.subheader("📸 Campus Gallery")

g1, g2 = st.columns(2)

with g1:
    st.image("campus2.jpg", use_container_width=True)
    st.image("campus3.jpg", use_container_width=True)
    st.image("campus4.jpg", use_container_width=True)

with g2:
    st.image("campus5.jpg", use_container_width=True)
    st.image("campus6.jpg", use_container_width=True)
    st.image("campus7.jpg", use_container_width=True)

st.divider()

# =====================================================
# AI ASSISTANT
# =====================================================

st.subheader("🤖 NCE AI Assistant")

question=st.text_input(
"Ask anything about NCE..."
)

if st.button("Search Answer"):

    q=question.lower().strip()

    if q in college_data["faq"]:
        st.success(college_data["faq"][q])

    else:
        st.warning(
        "Sorry! Information not found.\nGemini AI integration will answer this question in next version."
        )

st.divider()

# =====================================================
# CONTACT
# =====================================================

st.subheader("📞 Contact")

st.write("""
📍 Nalanda College of Engineering,
Chandi, Nalanda,
Bihar

🌐 https://ncechandi.ac.in

📧 Official College Email

☎ Official Contact Number
""")

st.divider()

st.markdown(
"""
<center>

### 🎓 NCE AI Campus Assistant

Made with ❤️ using Streamlit

</center>
""",
unsafe_allow_html=True
)
