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

# Title
st.title("🎓 NCE AI Campus Assistant")

st.write("### Welcome to Nalanda College of Engineering AI Assistant")
st.write("Ask anything about the college.")

# Show college name
st.success("College Name: " + college_data["college_name"])

# User input
user_question = st.text_input("Ask your question")

# Button
if st.button("Ask"):
    question = user_question.lower().strip()

    if question in college_data["faq"]:
        st.success(college_data["faq"][question])
    else:
        st.error("Sorry, I don't know the answer to this question yet.")
