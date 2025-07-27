# HTicket

A tool to match JIRA tickets with relevant code snippets from GitHub repositories and automatically fix issues.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with your credentials:

```
# Jira credentials
JIRA_EMAIL=your_jira_email@example.com
JIRA_TOKEN=your_jira_token_here
JIRA_DOMAIN=https://your-domain.atlassian.net

# GitHub credentials
GITHUB_TOKEN=your_github_token_here

# Gemini API credentials
GEMINI_MODEL_API_KEY=your_gemini_api_key_here
GEMINI_MODEL_URL=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent
```

> ⚠️ **Security Note**: Never commit your `.env` file or hardcode sensitive tokens in your code. The `.env` file is already added to `.gitignore`.

## Usage

### Processing a Ticket and Creating Fixes

Run the main script with a ticket ID:

```bash
python index.py TICKET-123
```

The script will:
1. Fetch the ticket description from JIRA
2. Find a matching GitHub repository based on the description
3. Fetch relevant code files from the repository
4. Use Gemini AI to generate a fix for the issue
5. Clone the repository
6. Create a branch named after the ticket
7. Apply the suggested code changes
8. Commit and push the changes
9. Optionally create a pull request

### Using the AI Model Separately

You can use the AI model component separately:

```bash
python Ai_model.py
```

This demonstrates a simple API call to the Gemini model.

## Files

- `index.py`: Main script containing the core functionality for processing tickets and implementing fixes
- `Constants.py`: Configuration file for loading environment variables
- `Ai_model.py`: Simple wrapper for the Gemini API
- `requirements.txt`: Project dependencies
- `.env`: Contains your API keys and credentials (not committed to git)

## Key Features

- **JiraClient**: Fetches ticket descriptions from JIRA
- **GitHubRepoScanner**: 
  - Identifies repositories based on ticket descriptions
  - Fetches code files and analyzes repository languages
  - Clones repositories and handles branch management
  - Applies code changes and creates pull requests
- **GeminiAnalyzer**: Uses Google's Gemini AI to analyze code and generate fixes
- **TicketFixAssistant**: Orchestrates the entire workflow

## Automated Fix Workflow

The automated fix process:

1. Fetches the ticket description from JIRA
2. Uses pattern matching to identify the relevant repository
3. Analyzes the repository's language composition
4. Fetches relevant code files 
5. Sends the code and ticket description to Gemini AI
6. Extracts code changes from the AI solution
7. Applies changes to the appropriate files
8. Creates a branch, commits changes and pushes to GitHub
9. Optionally creates a pull request

## Troubleshooting

- If you encounter JIRA authentication issues, verify your credentials in the `.env` file
- For GitHub API rate limits, ensure your token has appropriate permissions
- If repository identification fails, the system will attempt to extract keywords from the ticket description