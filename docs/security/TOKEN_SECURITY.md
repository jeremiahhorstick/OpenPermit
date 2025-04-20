# Secure Token Management

## Overview
This system provides a secure method for managing API tokens:
1. Tokens are stored in a protected directory
2. File permissions restrict access
3. Tokens are never committed to the repository
4. Token files are listed in .gitignore

## Usage
```python
from secure_tokens import get_grok_token
token = get_grok_token()
```

## Security Features
- Directory permissions: 700 (rwx------)
- Token file permissions: 600 (rw-------)
- Gitignore protection
- No environment variable exposure
