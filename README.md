# jwt-helper
CLI Utility to Decode Your JSON Web Tokens (JWT)

## Installation

1. Clone this repository:
   ```bash
   git clone <repo-url>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate your virtual environment:

   - For Mac or Linux:
     ```bash
     source .venv/bin/activate
     ```
   - For Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Review the Instructions

To review the instructions, use the `--help` flag:
```bash
python jwt-helper.py --help
```

### Example output:
```text
Usage: jwt-helper.py [OPTIONS]

Options:
  --jwt_token TEXT  Paste the JWT you would like to decode  [required]
  --help            Show this message and exit.
```

## How to Run the Helper Script

Run the helper script by providing the JWT token as a parameter. If no token is provided, you will be prompted to enter one.

### Example command:
```bash
python jwt-helper.py --jwt_token <your-jwt-token-here>
```

If you do not provide a token, the script will prompt you for one.

### Example Output:
```json
jwt: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```

## SHOW YOUR SUPPORT
Don't forget to give a ⭐️ if you found this repository useful!


## DISCLAIMER
THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.



