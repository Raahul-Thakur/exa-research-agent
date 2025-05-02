from phi.tools import Tool
from tools.exa_search import search_exa
from typing import ClassVar

# ✅ Custom ultra-minimal agent (no LLM, no config)
class ExaSearchTool(Tool):
    name: ClassVar[str] = "exa_search"
    description: ClassVar[str] = "Searches Exa.ai for research articles"
    type: ClassVar[str] = "tool"

    def run(self, query: str) -> str:
        return search_exa(query)

# ✅ Minimal agent wrapper class
class ResearchAgent:
    def __init__(self, tool: Tool):
        self.tool = tool

    def run(self, input: str):
        return self.tool.run(input)

# ✅ Create the agent instance with the Exa tool
research_agent = ResearchAgent(tool=ExaSearchTool(type="tool"))
