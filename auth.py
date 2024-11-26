import requests
import os
from dotenv import load_dotenv
import base64

# Load environment variables from a .env file
load_dotenv()

def get_token():
    # Retrieve client credentials from the .env file
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    # Ensure client credentials are provided
    if not client_id or not client_secret:
        raise ValueError("SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET not set in .env file")

    # Spotify API token URL
    url = 'https://accounts.spotify.com/api/token'

    # Create the authorization string
    auth_string = f"{client_id}:{client_secret}"
    auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

    # Set headers and form data
    headers = {
        'Authorization': f'Basic {auth_base64}'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=data)

    # Check for a successful response
    if not response.ok:
        raise Exception(f"Failed to retrieve token. Status code: {response.status_code}, Response: {response.json()}")
    
    access_token = response.json().get('access_token')

    return {
        'Authorization': f'Bearer {access_token}'
    }

if __name__ == '__main__':
    print(get_token())