import jwt
import json
import click

@click.command()
@click.option('--jwt_token',required=True, prompt='jwt',help='Paste the JWT you would like to decode')
def main(jwt_token:str):
    try:
        decoded_token = jwt.decode(jwt_token, options={"verify_signature": False})
        print(json.dumps(decoded_token, indent=2))
    except jwt.InvalidTokenError:
        print("The token is invalid.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
