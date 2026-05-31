import streamlit as st
import google.generativeai as genai
import os

# Set a premium dark-mode sports interface configuration
st.set_page_config(page_title="IPL AI Prompt War Arena", page_icon="⚡", layout="wide")

# Inject Custom CSS for an aggressive, competitive match-night aesthetic
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #ffffff; }
    h1 { color: #ff4b4b; text-align: center; font-weight: 800; letter-spacing: 1px; }
    div[data-testid="stMetricValue"] { color: #00f2fe; font-weight: bold; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 8px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ IPL AI PROMPT WAR ARENA ⚡")
st.markdown("<h4 style='text-align: center; color: #8a99ad;'>GDG Pune Live Value-Coding Challenge</h4>", unsafe_allow_html=True)
st.divider()

# Split the workspace layout into Match Input and Prompt Arena
col_left, col_right = st.columns([1, 2])

with col_left:
    st.subheader("📊 Live Match Context")
    batting = st.selectbox("Batting Team", ["RCB", "CSK", "MI", "KKR", "SRH"])
    bowling = st.selectbox("Bowling Team", ["CSK", "RCB", "MI", "KKR", "SRH"])
    
    c1, c2 = st.columns(2)
    with c1:
        runs = st.number_input("Runs Scored", value=164, min_value=0)
        overs = st.number_input("Overs (e.g., 17.2)", value=17.2, step=0.1)
    with c2:
        wickets = st.number_input("Wickets Down", value=5, min_value=0, max_value=10)
        target = st.number_input("Target Score", value=195)
        
    striker = st.text_input("Batsman on Strike", value="Virat Kohli")
    bowler = st.text_input("Current Bowler", value="Matheesha Pathirana")

with col_right:
    st.subheader("🔥 Deploy Tactical Prompt Challenge")
    user_prompt = st.text_area(
        "Enter your hyper-specific strategy prompt to challenge the AI script engine:",
        placeholder="Example: 'Virat Kohli spots the fine leg fielder moving wider, shuffles across off-stump, and scoops Pathirana for a boundary over fine leg...'",
        height=150
    )
    
    execute_war = st.button("🚀 UNLEASH PROMPT WAR")

st.divider()

# AI Engine Execution Logic
if execute_war:
    # Retrieve API key securely from Google Cloud Environment
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        st.error("Configuration Error: GEMINI_API_KEY environment variable is not defined.")
    elif not user_prompt:
        st.warning("The battle ground is empty! Please write a simulation prompt to challenge the engine.")
    else:
        with st.spinner("💥 Gemini AI is evaluating the context matrices..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.5-flash")
                
                # Context-aware orchestrator prompt
                master_prompt = f"""
                You are the ultimate IPL Prompt War Judge. Evaluate the user's tactical challenge prompt against the live cricket match situation.
                
                MATCH CONTEXT:
                - {batting} is chasing {target} runs against {bowling}.
                - Current Score: {runs}/{wickets} in {overs} overs.
                - Striker: {striker} | Bowler: {bowler}
                
                USER'S PROMPT CHALLENGE:
                "{user_prompt}"
                
                Generate a sharp, analytics-driven, and high-energy assessment in clean Markdown formatting with these exact sections:
                
                ### 🏆 Prompt Battle Score
                Provide a score out of 100 assessing how tactically brilliant and statistically realistic the user's scenario is given the current bowler/batsman dynamic, plus a 2-sentence reasoning.
                
                ### 🔮 The AI Scripted Outcome
                Simulate a detailed, ball-by-ball description of what happens next in the over. Merge the user's prompt intent seamlessly into high-stakes match reality.
                
                ### 🎯 Audience Engagement Micro-Bet
                Based on your scripted outcome, generate 1 instant multiple-choice question (with options A, B, C, D) for the live venue audience to vote on.
                """
                
                response = model.generate_content(master_prompt)
                
                st.success("🤖 Arena Battle Simulation Completed!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Arena System Failure: {str(e)}")

# Sidebar interaction widget for micro-predictions
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Fan Zone Prediction")
user_guess = st.sidebar.radio("Lock in your prediction for the next over:", ["Boundary", "Wicket", "1-5 Runs", "Dot Over"])
if st.sidebar.button("Submit Vote"):
    st.sidebar.success(f"Vote registered successfully for: {user_guess}")
