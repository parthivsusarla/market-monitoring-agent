import streamlit as st
from agent.agent import run_agent

st.set_page_config(page_title="Market Monitoring Agent", layout="centered")

st.title("📊 Market Monitoring AI Agent")

st.write("Track important market, policy, and tech developments.")

topic = st.text_input(
    "What should I monitor?",
    placeholder="Example: Indian stock market, gold prices, AI regulation"
)

if st.button("Analyze"):
    if not topic.strip():
        st.warning("Enter a topic to monitor.")
    else:
        with st.spinner("Analyzing latest developments..."):
            result = run_agent(topic)

        st.subheader("Analysis")
        st.markdown("### Result")
        st.markdown(result)

