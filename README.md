# jwt-helper
CLI Utility to Decode Your Java Web Tokens (JWT)

## Installation

1. Clone this repo. 
2. Create your venv ```python -m venv .venv```
3. Activate your virtual environment ```source .venv/bin/activate``` (for Mac or Linux) or ```.venv\script\activate``` (for Windows)
4. Install the required dependencies ```pip install -r requirements.txt```

## How to review the instructions

To review the instructions you can use the --help flag
```python jwt-helper.py --help
Usage: jwt-helper.py [OPTIONS]

Options:
  --jwt_token TEXT  Paste the JWT you would like to decode  [required]
  --help            Show this message and exit.
```
## How to run the helper script

Run the helper script providing the token as parameter or if not you will be prompted 
```bash
python jwt-helper.py
jwt: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```
