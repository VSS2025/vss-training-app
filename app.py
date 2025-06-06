import streamlit as st

# Page Config
st.set_page_config(page_title="VSS Training App", page_icon="🛡️", layout="centered")

# Session State Initialization
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'score' not in st.session_state:
    st.session_state.score = 0

# Functions for navigation
def go_to_course():
    st.session_state.page = 'course'

def go_to_quiz():
    st.session_state.page = 'quiz'

def submit_quiz():
    correct_answers = 2  # adjust if you change number of questions
    score = 0
    if st.session_state.q1 == "Observe and Report":
        score += 1
    if st.session_state.q2 == "True":
        score += 1
    st.session_state.score = score
    st.session_state.page = 'result'

def restart():
    st.session_state.page = 'home'
    st.session_state.score = 0

# Home Page
if st.session_state.page == 'home':
    st.title("🛡️ Valkyrie Security Solutions Training")
    st.header("Welcome to the Threat Assessment Training")
    st.write("Press start to begin your training.")
    if st.button("Start Training"):
        go_to_course()

# Course Content Page
elif st.session_state.page == 'course':
    st.title("Course: Introduction to Threat Assessment")
    st.image("https://via.placeholder.com/600x300.png?text=Course+Image", caption="Course Image Placeholder")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Placeholder video
    st.write("""
    **Overview:**
    
    Threat assessments are a proactive approach to identify and manage potential security threats before they escalate.
    
    Topics include:
    - Recognizing warning signs
    - Reporting procedures
    - Threat mitigation strategies
    """)
    if st.button("Start Quiz"):
        go_to_quiz()

# Quiz Page
elif st.session_state.page == 'quiz':
    st.title("Quiz: Test Your Knowledge")
    
    st.write("**1. What is the primary objective of a threat assessment?**")
    st.session_state.q1 = st.radio(
        "Choose one:",
        ["Detain the suspect", "Observe and Report", "Ignore minor threats", "Punish the offender"]
    )
    
    st.write("**2. True or False: Threat assessments are only necessary after an incident has occurred.**")
    st.session_state.q2 = st.radio(
        "Choose one:",
        ["True", "False"]
    )
    
    if st.button("Submit Answers"):
        submit_quiz()

# Result Page
elif st.session_state.page == 'result':
    st.title("Quiz Results")
    st.write(f"Your Score: {st.session_state.score} / 2")
    
    if st.session_state.score >= 2:
        st.success("Congratulations! You passed the course.")
    else:
        st.error("You did not pass. Please review the material and try again.")
    
    if st.button("Finish"):
        restart()
