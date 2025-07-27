# index.py - Main application file
import argparse
import sys
from Ai_model import GeminiAnalyzer
from Constants import JIRA_EMAIL, JIRA_TOKEN, JIRA_DOMAIN, GITHUB_TOKEN

class JiraClient:
    """Handles interactions with JIRA API"""
    
    def __init__(self):
        self.email = JIRA_EMAIL
        self.token = JIRA_TOKEN
        self.domain = JIRA_DOMAIN
        
        if not self.email or not self.token:
            print("ERROR: JIRA credentials not found in environment variables")
            sys.exit(1)
    
    def get_ticket_description(self, ticket_id):
        """Fetch ticket description from JIRA"""
        print(f"Fetching ticket {ticket_id} from JIRA...")
        # In a real implementation, this would make an API call
        # For demo purposes, returning mock data
        return f"Sample ticket description for {ticket_id}"

class GitHubRepoScanner:
    """Handles GitHub repository operations"""
    
    def __init__(self):
        self.token = GITHUB_TOKEN
        
        if not self.token:
            print("ERROR: GitHub token not found in environment variables")
            sys.exit(1)
    
    def find_repository(self, description):
        """Find relevant GitHub repository based on ticket description"""
        print(f"Finding repository based on description...")
        # Implementation would analyze the description and match with repos
        return "sample-repo"
    
    def fetch_code_files(self, repo_name):
        """Fetch relevant code files from repository"""
        print(f"Fetching code files from {repo_name}...")
        # Implementation would analyze repo and return relevant files
        return "def sample_function():\n    pass  # Implementation needed"
    
    def apply_changes(self, repo_name, file_path, changes):
        """Apply code changes and create a PR"""
        print(f"Applying changes to {file_path} in {repo_name}...")
        # Implementation would apply changes and create PR
        return True

class TicketFixAssistant:
    """Main workflow coordinator"""
    
    def __init__(self):
        self.jira_client = JiraClient()
        self.github_scanner = GitHubRepoScanner()
        self.ai_model = GeminiAnalyzer()
    
    def process_ticket(self, ticket_id):
        """Process a JIRA ticket and implement fixes"""
        
        # 1. Get ticket description from JIRA
        description = self.jira_client.get_ticket_description(ticket_id)
        print(f"Retrieved ticket description: {description[:50]}...")
        
        # 2. Find relevant GitHub repository
        repo_name = self.github_scanner.find_repository(description)
        print(f"Identified repository: {repo_name}")
        
        # 3. Fetch relevant code files
        code = self.github_scanner.fetch_code_files(repo_name)
        print("Fetched code files")
        
        # 4. Analyze code with AI and generate fix
        print("Analyzing code with Gemini AI...")
        ai_solution = self.ai_model.analyze_code(code, description)
        
        if not ai_solution:
            print("Failed to generate solution")
            return False
        
        print("AI solution generated")
        
        # 5. Apply code changes and create PR
        success = self.github_scanner.apply_changes(repo_name, "sample_file.py", "AI-generated solution")
        
        if success:
            print(f"Successfully implemented fix for ticket {ticket_id}")
            return True
        else:
            print(f"Failed to implement fix for ticket {ticket_id}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Process JIRA ticket and implement fixes.')
    parser.add_argument('ticket_id', help='JIRA ticket ID to process')
    args = parser.parse_args()
    
    assistant = TicketFixAssistant()
    assistant.process_ticket(args.ticket_id)

if __name__ == "__main__":
    main() 