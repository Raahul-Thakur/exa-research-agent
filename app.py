import os
import sys
import gradio as gr

from dotenv import load_dotenv
load_dotenv()
sys.path.append('./phidata')

# Import agent
from agents.research_agent import research_agent

def query_research_agent(user_query):
    if not user_query.strip():
        return "⚠️ Please enter a research topic."
    try:
        return research_agent.run(input=user_query)
    except Exception as e:
        return f"❌ Error: {str(e)}"

iface = gr.Interface(
    fn=query_research_agent,
    inputs=gr.Textbox(lines=2, placeholder="Enter your research query here..."),
    outputs="text",
    title="📚 Exa Research Agent",
    description="🔎 This AI agent uses Exa.ai to search the web for research articles and returns concise results.",
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()
