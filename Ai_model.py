# Ai_model.py - Simple wrapper for the Gemini API
import json
import requests
from Constants import GEMINI_MODEL_API_KEY, GEMINI_MODEL_URL

class GeminiAnalyzer:
    def __init__(self):
        self.api_key = GEMINI_MODEL_API_KEY
        self.api_url = GEMINI_MODEL_URL
        
    def analyze_code(self, code_snippet, ticket_description):
        """
        Analyze code and generate fixes based on ticket description
        """
        if not self.api_key:
            print("ERROR: GEMINI_MODEL_API_KEY not found in environment variables")
            return None
        
        prompt = self._create_prompt(code_snippet, ticket_description)
        response = self._call_gemini_api(prompt)
        return response
    
    def _create_prompt(self, code_snippet, ticket_description):
        """Create prompt for Gemini model"""
        return f"""
        TICKET DESCRIPTION:
        {ticket_description}
        
        CODE TO FIX:
        ```
        {code_snippet}
        ```
        
        Please analyze the code and provide fixes for the issues described in the ticket.
        Return your response in this format:
        
        ANALYSIS:
        [Your analysis of the issue]
        
        SOLUTION:
        [Your solution with code snippets]
        """
    
    def _call_gemini_api(self, prompt):
        """Make API call to Gemini model"""
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "contents": [{
                "parts":[{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.4,
                "topK": 32,
                "topP": 0.8,
                "maxOutputTokens": 2048,
            }
        }
        
        # Add API key as a query parameter
        url = f"{self.api_url}?key={self.api_key}"
        
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error calling Gemini API: {e}")
            return None

# Example usage
if __name__ == "__main__":
    analyzer = GeminiAnalyzer()
    
    # Simple test
    sample_code = "def add(a, b):\n    return a - b  # Bug here, should be addition"
    sample_description = "Fix the add function which is incorrectly doing subtraction"
    
    result = analyzer.analyze_code(sample_code, sample_description)
    
    if result:
        print("API Response:")
        print(json.dumps(result, indent=2))
    else:
        print("Failed to get response from Gemini API. Check your API key in .env file.")
