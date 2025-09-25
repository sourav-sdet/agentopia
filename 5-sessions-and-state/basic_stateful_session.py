import uuid
from dotenv import load_dotenv

from google.adk.runners import Runner 
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_and_answer_agent import question_and_answer_agent

load_dotenv()

# Create a new session service to store state
stateful_session_service = InMemorySessionService

# Store the initial state as a dictionary
initial_state = {
    "user_name": "Sourav Mishra",
    "user_preferences": """
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican.
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.
    """,
}

# Create a new session
APP_NAME = "Sourav Bot"
USER_ID = "Sourav"
SESSION_ID = str(uuid.uuid4())
stateful_session = stateful_session_service.create_session(
    app_name = APP_NAME,
    user_id = USER_ID,
    session_id = SESSION_ID,
    state = initial_state
)

print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

