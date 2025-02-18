import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import datetime
import json

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini AI function
def gemini_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Save progress locally
def save_progress(challenge, progress):
    data = {
        "date": str(datetime.now().date()),
        "challenge": challenge,
        "progress": progress
    }
    if not os.path.exists("progress.json"):
        with open("progress.json", "w") as f:
            json.dump([], f)

    with open("progress.json", "r") as f:
        logs = json.load(f)

    logs.append(data)
    with open("progress.json", "w") as f:
        json.dump(logs, f)

# Load progress
def load_progress():
    if not os.path.exists("progress.json"):
        return []
    with open("progress.json", "r") as f:
        return json.load(f)

st.title("🚀 Growth Mindset Challenge with Gemini AI")

# Intro Section
st.write(
    """
    **Adopt a Growth Mindset to unlock your full potential!**  
    - Embrace challenges 💪  
    - Learn from mistakes 🧠  
    - Stay persistent 🚀  
    """
)

# Daily Challenge Section
st.header("✨ Today's Growth Challenge")
challenge = st.text_input("What challenge will you tackle today?")
if st.button("Add Challenge"):
    st.success("Challenge added! Keep pushing forward! 🚀")

# Progress Log Section
st.header("📈 Track Your Progress")
progress = st.text_area("Reflect on what you learned today:")
if st.button("Log Progress"):
    save_progress(challenge, progress)
    st.success("Progress logged! You're on the path to growth! 🌱")

# Display previous logs
st.subheader("📅 Your Progress History")
logs = load_progress()
if logs:
    for log in logs[-5:]:
        st.write(f"**{log['date']}** - Challenge: {log['challenge']} | Progress: {log['progress']}")
else:
    st.write("No progress logged yet. Start your journey today!")

# Gemini AI Coach Section
st.sidebar.header("🧠 Ask Your Growth Mindset Coach")
user_question = st.sidebar.text_input("Ask any question about growth mindset:")
if st.sidebar.button("Get Advice"):
    with st.spinner("Your AI coach is thinking... 🤖"):
        response = gemini_response(user_question)
        st.sidebar.success(response)

# Streak Tracker
st.sidebar.header("🔥 Streak Tracker")
st.sidebar.write("Current Streak: 3 days 🔥")

# Motivational Quote
st.sidebar.markdown("---")
st.sidebar.subheader("💡 Daily Motivation")
quote = gemini_response("Give me a short motivational quote on growth mindset.")
st.sidebar.write(f"“{quote}”")

st.markdown("---")
st.markdown("Developed by Syeda Hafsa 🚀 | Powered by Gemini AI")
