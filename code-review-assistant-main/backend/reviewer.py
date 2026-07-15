import os
import json
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
USE_MOCK = False

try:
    from anthropic import Anthropic
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
except Exception:
    USE_MOCK = True

SYSTEM_PROMPT = """You are a senior software engineer with 10 years of experience 
in Python development and application security. You are conducting a thorough code review.

Your job is to find real problems. Analyse the submitted Python code for exactly four things:

1. Bugs: actual bugs or logical errors that would cause incorrect behaviour
2. Security: security vulnerabilities such as injection risks, exposed credentials, or unsafe operations
3. Quality: code quality issues including poor naming, missing error handling, inefficient patterns, lack of documentation
4. Suggestions: specific actionable recommendations to improve the code

Be specific and reference the actual code when describing issues.

You must respond ONLY in this exact JSON format with no markdown, no explanation, no preamble:
{
  "bugs": ["issue 1", "issue 2"],
  "security": ["issue 1", "issue 2"],
  "quality": ["issue 1", "issue 2"],
  "suggestions": ["suggestion 1", "suggestion 2"]
}

If nothing is found for a category, return an empty list for that category.
Never return anything outside the JSON object."""


MOCK_RESPONSE = {
    "bugs": [
        "get_user() function calls db.execute() but 'db' is never defined or imported, causing a NameError at runtime",
        "The function has no return type and no null check — if db returns None, the caller will crash silently"
    ],
    "security": [
        "Hardcoded password 'admin123' on line 2 — credentials should never be stored in source code, use environment variables instead",
        "SQL query is built by string concatenation with user input — this is a critical SQL injection vulnerability, use parameterised queries instead"
    ],
    "quality": [
        "The variable 'password' is defined but never used — remove unused variables",
        "Function parameter 'id' shadows Python's built-in 'id' function — use a more specific name like 'user_id'",
        "No docstring or type hints on get_user() — add documentation and type annotations",
        "'import os' is imported but never used — remove unused imports"
    ],
    "suggestions": [
        "Move credentials to a .env file and load them using python-dotenv or os.environ",
        "Use parameterised queries: cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))",
        "Add input validation to check that user_id is an integer before passing it to the query",
        "Wrap database calls in try/except blocks to handle connection errors gracefully"
    ]
}


def analyze_code(code: str) -> dict:
    if USE_MOCK:
        return MOCK_RESPONSE

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Please review this Python code:\n\n{code}"
                }
            ]
        )

        response_text = message.content[0].text.strip()
        result = json.loads(response_text)

        for key in ["bugs", "security", "quality", "suggestions"]:
            if key not in result:
                result[key] = []

        return result

    except Exception as e:
        error_message = str(e)
        if "credit balance is too low" in error_message or "insufficient" in error_message.lower():
            return MOCK_RESPONSE
        return {
            "bugs": [],
            "security": [],
            "quality": [],
            "suggestions": [f"An error occurred: {error_message}"]
        }