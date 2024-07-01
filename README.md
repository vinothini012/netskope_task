# Vulnerable Python Code (Educational Purpose)

**Warning:** This repository contains intentionally vulnerable code. Do not use in production. Use this code only for educational purposes to understand security vulnerabilities like SSRF and XSS and their mitigations.

## Setup
1. Install Flask: `pip install Flask`
2. Run the application: `python app.py`

## Vulnerabilities
### SSRF
Description: Server-Side Request Forgery example.
File: app.py (fetch function)
Mitigation: Validate URLs to ensure they are safe.

### XSS
Description: Cross-Site Scripting example.
File: app.py (greet function)
Mitigation: Sanitize user input using functions like `escape` from `markupsafe`.
