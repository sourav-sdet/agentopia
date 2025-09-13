from google.adk.agents import Agent 
from google.adk.tools import google_search


# This agent uses inbuilt tool - google_search

root_agent = Agent(
    name="google_search_tool_agent",
    model="gemini-2.0-flash",
    description="Google Search Tool Agent",
    instruction="""
    You are a helpful assistant that can use google_search tool
    """,
    tools=[google_search]
    # tools=[google_search]
    # tools=[google_search, custom_tool] --> this is not supported by adk
    #tools=[google_search, any_other_inbuilt_tool] --> this is not supported by adk
)