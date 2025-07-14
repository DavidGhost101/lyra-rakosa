import streamlit as st
from ultra_prompt import UltraOptimizedPromptGenerator

st.set_page_config(page_title="LYRA-RAKOSA Prompt Generator", layout="wide")

st.title("🚀 LYRA-RAKOSA Prompt Generator (20x Power Mode)")
st.markdown("This tool turns your task into an elite, structured AI prompt using the **4D Protocol + Chain Logic**.")

user_input = st.text_area("🔍 What do you want to ask the AI?", height=200)

if st.button("⚙️ Generate 20x Optimized Prompt"):
    if user_input.strip() == "":
        st.warning("Please enter a valid task or idea.")
    else:
        prompt_engine = UltraOptimizedPromptGenerator(user_input)
        st.success("✅ Prompt Generated Below")
        st.code(prompt_engine.apply_4d_methodology(), language='markdown')
