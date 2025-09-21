import os 
import random

from google.adk.agents import Agent

# LiteLLM is an interface that provides access to all LLM models
# from google.adk.models.litellm import LiteLLM

#model = LiteLLM(
#    model="openrouter/openai/gpt-41.1",
#    apikey=os.getenv("OPENROUTER_API_KEY")
#)


def get_dad_jokes():
    jokes=[
        "Why did the chicken cross the road? To get to the other side",
        "What do you call a belt made of watches? A waist of time",
        "What do you call fake spaghetti? An impasta",
        "Why did the scarecrow win an award? Because he was outstanding in his field"
    ]
    return random.choice(jokes)


root_agent = Agent(
    name="dad_joke_agent",
    model="gemini-2.0-flash",
    description="Dad Joke Agent",
    instruction="""
    You are a helpful assistant that can tell dad jokes, only use the tool "get_dad_jokes"
    """,
    tools=[get_dad_jokes]
)