# Constants.py - Configuration values
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Jira credentials
JIRA_EMAIL = os.environ.get("JIRA_EMAIL", "")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN", "")
JIRA_DOMAIN = os.environ.get("JIRA_DOMAIN", "https://capillarytech.atlassian.net")

# GitHub credentials
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Gemini API credentials
GEMINI_MODEL_API_KEY = os.environ.get("GEMINI_MODEL_API_KEY", "")
GEMINI_MODEL_URL = os.environ.get("GEMINI_MODEL_URL", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent") 