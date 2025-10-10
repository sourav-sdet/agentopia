import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from reminder_agent.agent import reminder_agent
from utils import call_agent_async

load_dotenv()

# ===== STEP 1: Initialize Persistent Session Service =====
# Using SQLite database for persistent storage
db_url = "sqlite:///./reminder_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)

# ===== STEP 2: Define Initial State =====
# This will only be used when creating a new session
initial_state = {
    "username": "Sourav Mishra",
    "reminders": [],
}

async def main_async():
    # Setup Constants
    APP_NAME="Reminder Agent"
    USER_ID="sourav_mishra"

    # ===== STEP 3: Session Management - Find or Create =====
    # Check for existing sessions for this user
    existing_sessions = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    # If there's an existing session, use it, otherwise create a new one
    if existing_sessions and len(existing_sessions) > 0:
        # Use the most recent session
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing with existing session: {SESSION_ID}")
    
    else:
        # Create a new session with initial state
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created a new session: {SESSION_ID}")

    # ===== STEP 4: Agent Runner Setup =====
    # Create a runner with the memory agent
