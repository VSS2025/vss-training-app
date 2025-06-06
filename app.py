import streamlit as st
import random
from fpdf import FPDF
from datetime import date

# Page Config
st.set_page_config(page_title="VSS Training App", page_icon="🛡️", layout="centered")

# Session State Initialization
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0
if 'selected_course' not in st.session_state:
    st.session_state.selected_course = None
if 'quiz_questions' not in st.session_state:
    st.session_state.quiz_questions = []
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Slide and Quiz Bank
courses = {
    "Stop the Bleed": {
        "slides": [
            "Recognize life-threatening bleeding.",
            "Find the source of bleeding.",
            "Apply firm, direct pressure.",
            "Use dressings or clean cloths.",
            "Pack (stuff) wounds if needed.",
            "Apply a tourniquet if direct pressure is not effective.",
            "Tourniquet placement 2-3 inches above the wound.",
            "Tighten until bleeding stops.",
            "Do not remove tourniquet once applied.",
            "Call 911 as soon as possible.",
            "Monitor victim for shock.",
            "Keep victim warm.",
            "Reassure and support victim emotionally.",
            "Continue monitoring until emergency services arrive.",
            "Practice these skills regularly."
        ],
        "quiz_pool": [
            {"question": "What is the first step when you encounter severe bleeding?", "options": ["Apply pressure", "Call 911", "Clean the wound", "Look for help"], "answer": "Apply pressure"},
            {"question": "The best way to stop life-threatening bleeding is:", "options": ["Ice", "Pressure", "Elevation", "Tourniquet"], "answer": "Pressure"},
            {"question": "Where should a tourniquet be placed?", "options": ["Directly on the wound", "Below the wound", "Above the wound", "Next to the wound"], "answer": "Above the wound"},
            {"question": "When should you remove a tourniquet?", "options": ["Every 15 minutes", "After bleeding stops", "When EMS arrives", "Never until medical help takes over"], "answer": "Never until medical help takes over"},
            {"question": "What is the primary cause of preventable death in trauma?", "options": ["Bleeding", "Broken bones", "Burns", "Shock"], "answer": "Bleeding"},
            {"question": "If a tourniquet is not available, what should you use?", "options": ["Loose cloth", "Firm direct pressure", "Ice pack", "Band-aid"], "answer": "Firm direct pressure"},
            {"question": "Which material is ideal for packing wounds?", "options": ["Cloth or gauze", "Plastic", "Cotton balls", "Newspaper"], "answer": "Cloth or gauze"},
            {"question": "Life-threatening bleeding can cause death in:", "options": ["Minutes", "Hours", "Days", "Weeks"], "answer": "Minutes"},
            {"question": "Signs of shock include:", "options": ["Rapid breathing", "Slurred speech", "Dry skin", "Hives"], "answer": "Rapid breathing"},
            {"question": "After applying a tourniquet, what must you do?", "options": ["Loosen it every 5 minutes", "Keep it in place", "Add ice", "Remove it once bleeding stops"], "answer": "Keep it in place"},
            {"question": "High-risk areas for serious bleeding injuries include:", "options": ["Head", "Chest", "Legs", "All of the above"], "answer": "All of the above"},
            {"question": "True or False: Bleeding always stops on its own.", "options": ["True", "False"], "answer": "False"},
            {"question": "The first priority when treating a victim is to:", "options": ["Ensure your safety", "Check for ID", "Remove clothing", "Take a picture"], "answer": "Ensure your safety"},
            {"question": "Tourniquets should be placed:", "options": ["As close to the wound as possible", "Over a joint", "At least 2-3 inches above the wound", "On the hand"], "answer": "At least 2-3 inches above the wound"},
            {"question": "What does ‘Stop the Bleed’ primarily teach?", "options": ["Wound cleaning", "Bleeding control", "Medication application", "Suturing"], "answer": "Bleeding control"},
            {"question": "Packing a wound helps to:", "options": ["Create clotting", "Cool the wound", "Remove debris", "Cause pain"], "answer": "Create clotting"},
            {"question": "What should be avoided when treating a bleeding victim?", "options": ["Direct pressure", "Removing clots", "Using gauze", "Calling 911"], "answer": "Removing clots"},
            {"question": "You should press on a wound for at least:", "options": ["30 seconds", "1 minute", "5 minutes", "Until EMS arrives"], "answer": "Until EMS arrives"},
            {"question": "Best placement for a second tourniquet is:", "options": ["Below the first", "Above the first", "On the hand", "Next to the wound"], "answer": "Above the first"},
            {"question": "What is a common improvised tourniquet?", "options": ["Rope and stick", "Elastic band", "Plastic bag", "Towel"], "answer": "Rope and stick"},
            {"question": "When treating bleeding, gloves are important to:", "options": ["Stay clean", "Look professional", "Prevent infection", "Keep warm"], "answer": "Prevent infection"},
            {"question": "Bleeding from which location is most life-threatening?", "options": ["Scalp", "Chest", "Fingertip", "Elbow"], "answer": "Chest"},
            {"question": "What is the goal of applying pressure?", "options": ["Stop bleeding", "Slow bleeding", "Relieve pain", "Open the wound"], "answer": "Stop bleeding"},
            {"question": "Bleeding control should start:", "options": ["After checking vitals", "Immediately", "After bandaging", "Only if unconscious"], "answer": "Immediately"},
            {"question": "If bleeding soaks through a bandage, you should:", "options": ["Remove and replace", "Add another bandage on top", "Ignore it", "Loosen it"], "answer": "Add another bandage on top"}
        ]
    },
    "Active Assailant (Run, Hide, Fight)": {
        "slides": [
            "Be aware of your environment.",
            "Have an exit plan.",
            "RUN if you can safely escape.",
            "Leave belongings behind.",
            "Help others escape if possible.",
            "HIDE if escape is not possible.",
            "Lock and barricade doors.",
            "Silence electronic devices.",
            "Stay out of the attacker’s view.",
            "Prepare to FIGHT as a last resort.",
            "Be aggressive and commit to your actions.",
            "Improvise weapons (fire extinguisher, chair, etc.).",
            "Incapacitate the attacker.",
            "Call 911 when safe to do so.",
            "Stay calm and follow law enforcement instructions."
        ],
        "quiz_pool": [
            {"question": "What is your first response if there is an active shooter?", "options": ["Run", "Hide", "Fight", "Call 911"], "answer": "Run"},
            {"question": "If you can’t run, you should:", "options": ["Hide", "Fight", "Freeze", "Surrender"], "answer": "Hide"},
            {"question": "When hiding, you should:", "options": ["Lock doors", "Stay visible", "Make noise", "Hide under a desk"], "answer": "Lock doors"},
            {"question": "Final option if your life is in danger:", "options": ["Run", "Hide", "Fight", "Negotiate"], "answer": "Fight"},
            {"question": "If you escape safely, your next action is:", "options": ["Call 911", "Call family", "Go home", "Go back"], "answer": "Call 911"},
            {"question": "When running from an active assailant:", "options": ["Bring all your stuff", "Leave belongings", "Hide valuables", "Wave for help"], "answer": "Leave belongings"},
            {"question": "Best hiding spot has:", "options": ["Minimal cover", "Good locks and no visibility", "A window view", "An open exit"], "answer": "Good locks and no visibility"},
            {"question": "If law enforcement arrives:", "options": ["Run to them", "Raise your hands", "Yell directions", "Grab their weapons"], "answer": "Raise your hands"},
            {"question": "If hiding, silence:", "options": ["Phones", "Radios", "Alarms", "All of the above"], "answer": "All of the above"},
            {"question": "True or False: You should confront the assailant if possible.", "options": ["True", "False"], "answer": "False"},
            {"question": "What improvised weapon is most effective?", "options": ["Chair", "Pencil", "Trash can", "Bottle"], "answer": "Chair"},
            {"question": "Main goal in active shooter situation:", "options": ["Evacuate safely", "Get closer", "Negotiate", "Take video"], "answer": "Evacuate safely"},
            {"question": "If you hide, barricade by:", "options": ["Locking doors", "Piling heavy objects", "Both", "Neither"], "answer": "Both"},
            {"question": "Should you pull the fire alarm?", "options": ["Yes", "No"], "answer": "No"},
            {"question": "Best time to fight:", "options": ["At first sight", "If running/hiding fails", "After 10 minutes", "Never"], "answer": "If running/hiding fails"},
            {"question": "Effective action when fighting:", "options": ["Commit to your actions", "Be hesitant", "Wait for backup", "Call 911"], "answer": "Commit to your actions"},
            {"question": "Run away from:", "options": ["Shooter’s sight", "Shooter’s back", "Police", "Exit signs"], "answer": "Shooter’s sight"},
            {"question": "What to do during lockdown drills?", "options": ["Ignore", "Practice Run/Hide/Fight", "Post online", "Leave early"], "answer": "Practice Run/Hide/Fight"},
            {"question": "Stay hidden until:", "options": ["Police give all-clear", "You feel safe", "Shooter leaves", "Alarm stops"], "answer": "Police give all-clear"},
            {"question": "When hiding, avoid:", "options": ["Windows", "Locking doors", "Silencing phones", "Covering lights"], "answer": "Windows"},
            {"question": "True or False: Fighting increases your survival chances if run and hide aren't options.", "options": ["True", "False"], "answer": "True"},
            {"question": "When escaping, what should you show?", "options": ["Empty hands", "Badge", "Backpack", "Cell phone"], "answer": "Empty hands"},
            {"question": "If barricading, use:", "options": ["Furniture", "Curtains", "Pillows", "Shoes"], "answer": "Furniture"},
            {"question": "Run direction should be:", "options": ["To the shooter", "Away from the shooter", "In a circle", "Downward"], "answer": "Away from the shooter"},
            {"question": "When running, keep your hands:", "options": ["Hidden", "Waving", "Visible", "Closed"], "answer": "Visible"}
        ]
    }
}

# Certificate Generator
def generate_certificate(user_name, course_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.cell(200, 40, "Certificate of Completion", ln=True, align='C')
    pdf.set_font("Arial", "", 16)
    pdf.cell(200, 10, f"This is to certify that", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", "B", 20)
    pdf.cell(200, 10, user_name, ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", "", 16)
    pdf.cell(200, 10, f"has successfully completed the course", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, 10, course_name, ln=True, align='C')
    pdf.ln(20)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Date: {date.today().strftime('%B %d, %Y')}", ln=True, align='C')
    return pdf.output(dest='S').encode('latin-1')

# Navigation functions
def go_to_course(course_name):
    st.session_state.selected_course = course_name
    st.session_state.current_slide = 0
    st.session_state.page = 'slides'

def go_to_quiz():
    pool = courses[st.session_state.selected_course]["quiz_pool"]
    st.session_state.quiz_questions = random.sample(pool, min(15, len(pool)))
    st.session_state.quiz_answers = {}
    st.session_state.page = 'quiz'

def submit_quiz():
    correct = 0
    for i, q in enumerate(st.session_state.quiz_questions):
        if st.session_state.quiz_answers.get(i) == q["answer"]:
            correct += 1
    st.session_state.score = correct
    if correct >= 12:
        st.session_state.page = 'certificate'
    else:
        st.session_state.page = 'fail'

def restart():
    st.session_state.page = 'home'
    st.session_state.score = 0
    st.session_state.selected_course = None
    st.session_state.current_slide = 0
    st.session_state.user_name = ""

# Page Handling
if st.session_state.page == 'home':
    st.title("🛡️ Valkyrie Security Solutions Training")
    st.header("Choose a Course:")
    for course_name in courses.keys():
        if st.button(f"Start {course_name}"):
            go_to_course(course_name)

elif st.session_state.page == 'slides':
    slides = courses[st.session_state.selected_course]["slides"]
    st.title(f"{st.session_state.selected_course}")
    st.subheader(f"Slide {st.session_state.current_slide + 1} of {len(slides)}")
    st.write(slides[st.session_state.current_slide])

    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.session_state.current_slide > 0:
            if st.button("Previous"):
                st.session_state.current_slide -= 1
    with col3:
        if st.session_state.current_slide < len(slides) - 1:
            if st.button("Next"):
                st.session_state.current_slide += 1
        else:
            if st.button("Start Quiz"):
                go_to_quiz()

elif st.session_state.page == 'quiz':
    st.title(f"Quiz: {st.session_state.selected_course}")
    for i, q in enumerate(st.session_state.quiz_questions):
        st.write(f"**{i+1}. {q['question']}**")
        st.session_state.quiz_answers[i] = st.radio(
            f"Question {i+1}",
            q["options"],
            index=None,               # 👈 this is the part we added
            key=f"q{i}"
        )
    if st.button("Submit Answers"):
        submit_quiz()

elif st.session_state.page == 'fail':
    st.title("Quiz Results")
    st.error(f"You scored {st.session_state.score}/15. You did not pass. Please review the material and try again.")
    if st.button("Retry"):
        restart()

elif st.session_state.page == 'certificate':
    st.title("Congratulations!")
    st.success(f"You scored {st.session_state.score}/15. You passed!")
    st.write("Please enter your name for the certificate:")
    st.session_state.user_name = st.text_input("Name")
    if st.session_state.user_name:
        cert = generate_certificate(st.session_state.user_name, st.session_state.selected_course)
        st.download_button(
            label="Download Certificate",
            data=cert,
            file_name="certificate.pdf",
            mime="application/pdf"
        )
    if st.button("Finish"):
        restart()
